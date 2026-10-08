from django.contrib import admin

# Register your models here.
from .models import Channel, Workspace, WorkspaceMembership


@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):
	list_display = ("name", "created_by", "created_at")
	search_fields = ("name", "created_by__username")


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
	list_display = ("name", "workspace", "created_at")
	list_filter = ("workspace",)
	search_fields = ("name", "workspace__name")


@admin.register(WorkspaceMembership)
class WorkspaceMembershipAdmin(admin.ModelAdmin):
	list_display = ("user", "workspace", "role", "created_at")
	list_filter = ("role", "workspace")
	search_fields = ("user__username", "workspace__name")
