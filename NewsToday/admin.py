from django.contrib import admin

from NewsToday.models import Category

# Register your models here.

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['cat_name']