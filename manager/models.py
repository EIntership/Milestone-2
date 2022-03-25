from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


PRIORITY = (
    ('NONE', 'None'),
    ('LOW', 'Low'),
    ('Medium', 'Medium'),
    ('HIGH', 'High'),
)



class Task(models.Model):
    name = models.CharField(max_length=35)
    description = models.TextField()
    public = models.BooleanField(default=False, )
    date = models.DateTimeField(auto_now_add=True)
    date_finished = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(
        max_length=6,
        choices=PRIORITY,
        default='NONE',
        db_index=True
    )
    complited = models.BooleanField('complited', default=False)
    user = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='users'
    )

    def __str__(self):
        return self.name


class TaskList(models.Model):
    task = models.ManyToManyField(Task, blank=True)
    name = models.CharField(max_length=250, unique=False)

    def __str__(self):
        return self.name


class Project(models.Model):
    tasklist = models.ForeignKey(TaskList, related_name="project", null=True, on_delete=models.CASCADE)
    name = models.CharField(null=True, max_length=250)
    description = models.TextField()
    user = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True
    )

    def __str__(self):
        return self.name
