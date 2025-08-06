from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from notes.models import Notification, UserContactInfo, NotificationLog


@admin.register(Notification)
class MyUserAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'message',
        'created_at',
    )
    search_fields = ('user',)


@admin.register(UserContactInfo)
class UserContactInfoAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'email',
        'phone',
    )
    search_fields = ('user',)


@admin.register(NotificationLog)
class NotificationLogAdmin(admin.ModelAdmin):

    list_display = (
        'notification',
        'channel',
        'created_at',
    )
    search_fields = ('notification',)
