from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


if admin.site.is_registered(User):
    admin.site.unregister(User)

admin.site.register(User, UserAdmin)
