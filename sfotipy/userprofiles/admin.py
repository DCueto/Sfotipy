from django.contrib import admin

from .models import UserTrack, UserProfile

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserTrack)