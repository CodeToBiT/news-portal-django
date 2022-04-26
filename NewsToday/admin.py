from django.contrib import admin

from NewsToday.models import *

# Register your models here.

@admin.register(Category)

class AdminCategory(admin.ModelAdmin):
    list_display = ['cat_name']

@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display = ['news_title']

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ['contact_name']

@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ['comment_content']