from rest_framework import serializers
from apps.managers.models import Task,  Comment
from django.core.mail import EmailMessage


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name']


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
        fields = ['id', 'name', 'description', 'completed', 'user']


class AssignTaskToUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['user']

    def update(self, instance, validated_data):
        to = []
        for user in validated_data.get('user', []):
            if not getattr(user, "email", None):
                continue
            to.append(user.email)

        email = EmailMessage(
            'Test mail',
            'Task was assigned to you',
            '8e42ade77ab934',
            to
        )
        print(validated_data)
        email.fail_silently = False
        email.send()
        return super(AssignTaskToUserSerializer, self).update(instance, validated_data)


class CompleteTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'completed']

    def update(self, instance, validated_data):
        instance.completed = not instance.completed
        to = []
        users = instance.user.all()
        for user in users:
            if not getattr(user, "email", None):
                continue
            to.append(user.email)
        
        email = EmailMessage(
            'Test mail',
            'You complit a task',
            '8e42ade77ab934',
            to
        )
    
        email.fail_silently = False
        email.send()
        return super(CompleteTaskSerializer, self).update(instance, validated_data)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['task', 'comment']


class ViewCommentsSerializer(serializers.ModelSerializer):
    task_comment = CommentSerializer(many=True)
    class Meta:
        model = Task
        fields = ['task_comment']
