from django.contrib import admin
from .models import Pack


@admin.register(Pack)
class PackAdmin(admin.ModelAdmin):
    list_display = ('title',)
