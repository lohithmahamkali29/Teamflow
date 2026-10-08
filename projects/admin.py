from django.contrib import admin

from .models import Project, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "workspace", "created_by", "created_at")
    list_filter = ("workspace",)
    search_fields = ("name", "workspace__name", "created_by__username")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "status", "priority", "assigned_to")
    list_filter = ("status", "priority", "project__workspace")
    search_fields = ("title", "project__name", "assigned_to__username")