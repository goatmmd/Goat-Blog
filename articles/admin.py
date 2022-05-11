from django.contrib import admin
from django.contrib.admin import register

from articles.models import Post, Comment, Category


class CommentAdminTabularInline(admin.TabularInline):
    model = Comment
    extra = 10


@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'body', 'created_time', 'modified_time')
    list_editable = ('status',)
    inlines = [CommentAdminTabularInline]


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_id')
