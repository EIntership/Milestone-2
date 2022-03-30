from rest_framework import generics, permissions
from apps.managers.models import  Task, Comment
from rest_framework.generics import  get_object_or_404
from apps.managers.serializers import (
    TaskSerializer,
    CreatetaskSerializer,
    TaskDetailsSerializer,
    AssignTaskToUserSerializer,
    CompleteTaskSerializer,
    CommentSerializer,
    ViewCommentsSerializer)
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.


class TaskView(generics.ListCreateAPIView, generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ['name']


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
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)


class CompletedTaskView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(completed=True)


class AssignTaskToUser(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AssignTaskToUserSerializer
    queryset = Task.objects.all()


class CompleteTaskView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CompleteTaskSerializer
    queryset = Task.objects.all()



class CommentAddView(generics.CreateAPIView):
    permissions_classes = (permissions.IsAuthenticated,)
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentView(generics.ListAPIView):
    permissions_classes = (permissions.IsAuthenticated,)
    serializer_class = ViewCommentsSerializer

    def get(self, request, pk):
        task = get_object_or_404(Task.objects.filter(pk=pk))
        return Response(ViewCommentsSerializer(task).data)
