import os
import platform
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserPCSpecForm, ReviewForm
from .models import UserPCSpec, Game, Review
import psutil
import cpuinfo

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f"Welcome {username}, your account has been created.")
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('index')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('index')

def get_pc_specs():
    cpu_info = cpuinfo.get_cpu_info()
    specs = {
        'cpu': cpu_info['brand_raw'],  # This provides a user-friendly CPU name
        'gpu': 'N/A',  # You may need a third-party library to fetch GPU info
        'ram': round(psutil.virtual_memory().total / (1024. ** 3)),  # GB
        'storage': round(psutil.disk_usage('/').total / (1024. ** 3)),  # GB
        'os_version': platform.version(),
    }
    return specs

@login_required
def collect_pc_specs(request):
    if request.method == 'POST':
        if 'get_specs' in request.POST:
            # Fetch and prefill PC specs into the form
            specs = get_pc_specs()
            form = UserPCSpecForm(initial=specs)
        else:
            # Save form data
            form = UserPCSpecForm(request.POST)
            if form.is_valid():
                UserPCSpec.objects.update_or_create(user=request.user, defaults=form.cleaned_data)
                return redirect('list_games')
    else:
        form = UserPCSpecForm()

    return render(request, 'collect_pc_specs.html', {'form': form})

@login_required
def list_games(request):
    games = Game.objects.all()
    return render(request, 'list_games.html', {'games': games})

@login_required
def check_compatibility(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    user_pc_spec = get_object_or_404(UserPCSpec, user=request.user)

    compatible = (user_pc_spec.cpu >= game.min_cpu and
                  user_pc_spec.gpu >= game.min_gpu and
                  user_pc_spec.ram >= game.min_ram and
                  user_pc_spec.storage >= game.min_storage and
                  user_pc_spec.os_version >= game.min_os_version)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.game = game
            review.save()
            return redirect('check_compatibility', game_id=game.id)
    else:
        review_form = ReviewForm()

    reviews = Review.objects.filter(game=game)

    context = {
        'game': game,
        'compatible': compatible,
        'review_form': review_form,
        'reviews': reviews,
    }
    return render(request, 'check_compatibility.html', context)
from django.http import JsonResponse

def fetch_pc_specs(request):
    # Check if the request is an AJAX request
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        specs = get_pc_specs()
        return JsonResponse(specs)
    return JsonResponse({'error': 'Invalid request'}, status=400)
