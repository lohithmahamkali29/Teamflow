from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
from django.test import TestCase

from chat.models import ChatMessage
from projects.models import Project, Task
from workspaces.models import Channel, Workspace, WorkspaceMembership


class WorkspaceMembershipTests(TestCase):
    def setUp(self):
        user_model = get_user_model()
        self.user = user_model.objects.create_user(username="member")
        self.workspace = Workspace.objects.create(
            name="Engineering", created_by=self.user
        )

    def test_membership_is_unique_per_workspace_and_user(self):
        WorkspaceMembership.objects.create(user=self.user, workspace=self.workspace)

        with self.assertRaises(IntegrityError), transaction.atomic():
            WorkspaceMembership.objects.create(user=self.user, workspace=self.workspace)

    def test_model_string_representations(self):
        channel = Channel.objects.create(name="general", workspace=self.workspace)
        membership = WorkspaceMembership.objects.create(
            user=self.user, workspace=self.workspace
        )
        message = ChatMessage.objects.create(
            channel=channel, sender=self.user, content="Hello team"
        )

        self.assertEqual(str(self.workspace), "Engineering")
        self.assertEqual(str(channel), "Engineering / general")
        self.assertEqual(str(membership), "member - Engineering")
        self.assertEqual(str(message), "member in Engineering / general: Hello team")


class ProjectAndTaskTests(TestCase):
    def setUp(self):
        user_model = get_user_model()
        self.creator = user_model.objects.create_user(username="creator")
        self.assignee = user_model.objects.create_user(username="assignee")
        self.workspace = Workspace.objects.create(
            name="Engineering", created_by=self.creator
        )

    def test_project_creation_and_string_representation(self):
        project = Project.objects.create(
            workspace=self.workspace,
            name="Roadmap",
            created_by=self.creator,
        )

        self.assertEqual(project.workspace, self.workspace)
        self.assertEqual(str(project), "Engineering / Roadmap")

    def test_task_defaults_and_assignment_options(self):
        project = Project.objects.create(
            workspace=self.workspace,
            name="Roadmap",
            created_by=self.creator,
        )
        unassigned_task = Task.objects.create(
            project=project,
            title="Plan milestones",
            created_by=self.creator,
        )
        assigned_task = Task.objects.create(
            project=project,
            title="Review milestones",
            created_by=self.creator,
            assigned_to=self.assignee,
        )

        self.assertEqual(unassigned_task.status, Task.Status.TODO)
        self.assertEqual(unassigned_task.priority, Task.Priority.MEDIUM)
        self.assertIsNone(unassigned_task.assigned_to)
        self.assertEqual(assigned_task.assigned_to, self.assignee)
        self.assertEqual(str(unassigned_task), "Plan milestones")