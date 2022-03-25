from rest_framework import serializers
from .models import Task, TaskList, Project
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name']


class MyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = '__all__'


class ProjectSerialize(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class CreatetaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'description']

    def create(self, validated_data):
        request = self.context['request']
        if user := request.user:
            validated_data.update({
                'user': [user]
            })
        return super(CreatetaskSerializer, self).create(validated_data)


class TaskDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'complited', 'user']


class AssignTaskToUserSerealizator(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['user']


class CompleteTaskSerializator(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'complited']