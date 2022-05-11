from django.contrib import admin
from django.contrib.admin import register

from members.models import UserProfile, UserProfileAttribute


class UserProfileAttributeInlineAdmin(admin.TabularInline):
    model = UserProfileAttribute
    extra = 5


@register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )
    inlines = [UserProfileAttributeInlineAdmin]
