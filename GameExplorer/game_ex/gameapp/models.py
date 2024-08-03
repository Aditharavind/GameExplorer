from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserPCSpec(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    cpu = models.CharField(max_length=100)
    gpu = models.CharField(max_length=100)
    ram = models.IntegerField(help_text="RAM in GB")
    storage = models.IntegerField(help_text="Storage in GB")
    os_version = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username}'s PC Specs"

class Game(models.Model):
    title = models.CharField(max_length=100)
    min_cpu = models.CharField(max_length=100)
    min_gpu = models.CharField(max_length=100)
    min_ram = models.IntegerField(help_text="Minimum RAM in GB")
    min_storage = models.IntegerField(help_text="Minimum Storage in GB")
    min_os_version = models.CharField(max_length=100)

    def __str__(self):
        return self.title
class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.game.name} - {self.rating}"