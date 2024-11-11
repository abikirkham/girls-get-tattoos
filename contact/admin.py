from django.contrib import admin
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'read', 'mark_as_read')
    list_filter = ('read',)
    actions = ['mark_messages_as_read']

    def mark_as_read(self, obj):
        return not obj.read

    mark_as_read.short_description = 'Read/Unread'
    mark_as_read.boolean = True

    def mark_messages_as_read(self, request, queryset):
        queryset.update(read=True)
    mark_messages_as_read.short_description = 'Mark selected messages as read'

admin.site.register(ContactMessage, ContactMessageAdmin)
