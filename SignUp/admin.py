from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class UserAdmin(UserAdmin, admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'is_staff', 'profileImg')

admin.site.register(User, UserAdmin)
