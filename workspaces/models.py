from django.db import models
from django.conf import settings
# Create your models here.
class Workspace(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name = "created_workspaces")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Channel (models.Model):
    name = models.CharField(max_length=100)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name='channels')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'workspace'], name='unique_channel_name_per_workspace')
        ]

class WorkspaceMembership(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="workspace_memberships"
    )
    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        related_name="memberships"
    )
    role = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('member', 'Member')])
    joined_at = models.DateTimeField(auto_now_add=True)

class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'workspace'], name='unique_user_workspace_membership')
        ]
    
def __str__(self):
        return f"{self.user.username} - {self.workspace.name}"