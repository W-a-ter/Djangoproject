from django.contrib import admin

from .models import User


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    """Отображает в админке пользователей"""
    list_display = ('id', 'username', 'email', 'phone_number', 'country',)
    list_filter = ('country',)
    search_fields = ('id', 'username', 'email', 'country',)
