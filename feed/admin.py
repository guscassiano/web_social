from django.contrib import admin
from .models import PostModel


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'message', 'created_at')
    search_fields = ('title', 'author')

admin.site.register(PostModel, PostAdmin)