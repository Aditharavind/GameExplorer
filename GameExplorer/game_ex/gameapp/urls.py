from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('collect_pc_specs/', views.collect_pc_specs, name='collect_pc_specs'),
    path('games/', views.list_games, name='list_games'),
    path('games/<int:game_id>/check/', views.check_compatibility, name='check_compatibility'),
    path('get_pc_specs/', views.fetch_pc_specs, name='fetch_pc_specs'),
]
