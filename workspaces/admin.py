from django.contrib import admin

# Register your models here.
from .models import Workspace, Channel, WorkspaceMembership

admin.site.register(Workspace)
admin.site.register(Channel)
admin.site.register(WorkspaceMembership)
