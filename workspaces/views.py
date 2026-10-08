from django.shortcuts import render
from rest_framework.views import APIView
from .models import Workspace
from .serializers import WorkspaceSerializer
from rest_framework.response import Response


# Create your views here.
class WorkspaceListView(APIView):

    def get(self, request):
        workspaces = Workspace.objects.all()
        serializer = WorkspaceSerializer(workspaces, many=True)
        return Response(serializer.data)
