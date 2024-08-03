from django.contrib import admin

from .models import UserPCSpec, Game, Review

# Register your models here.
admin.site.register(UserPCSpec)
admin.site.register(Game)
admin.site.register(Review)