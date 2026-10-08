from django.contrib import admin

# Register your models here.
from .models import ChatMessage


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
	list_display = ("sender", "channel", "created_at")
	list_filter = ("channel", "created_at")
	search_fields = ("content", "sender__username", "channel__name")