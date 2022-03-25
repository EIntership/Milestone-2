from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.views import APIView

from .models import Project, Task, TaskList
from rest_framework.generics import GenericAPIView, get_object_or_404
from .serializers import ProjectSerialize, TaskSerializer, TaskListSerializer, UsersListSerializer, \
    CreatetaskSerializer, TaskDetailsSerializer, MyTaskSerializer, AssignTaskToUserSerealizator, \
    CompleteTaskSerializator
from django.contrib.auth.models import User
from rest_framework.response import Response


# Create your views here.

class ProjectView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerialize


class TaskView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskListView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class UsersListView(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UsersListSerializer


class CreateTaskView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = CreatetaskSerializer


class TaskDetailView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TaskDetailsSerializer

    def get(self, request, pk):
        task = get_object_or_404(Task.objects.filter(pk=pk))
        return Response(TaskDetailsSerializer(task).data)


class MyTaskView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = MyTaskSerializer

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)


class CompletedTaskView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = MyTaskSerializer

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user, complited=True)


class AssignTokenToUser(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AssignTaskToUserSerealizator
    queryset = Task.objects.all()


class ComplitTaskView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CompleteTaskSerializator
    queryset = Task.objects.filter(complited=False)
