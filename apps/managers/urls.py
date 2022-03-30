from django.urls import path
from apps.managers.views import (
    CreateTaskView,
    TaskView,
    TaskDetailView,
    MyTaskView,
    CompletedTaskView,
    AssignTaskToUser,
    CompleteTaskView,
    CommentAddView,
    CommentView)

urlpatterns = [
    #path('taskcreate', CreateTaskView.as_view(), name='CreateTaskView'),
    path('task', TaskView.as_view(), name='CreateTaskView'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='Task-info-View'),
    path('mytask', MyTaskView.as_view(), name='My-Task-View'),
    path('compited-task', CompletedTaskView.as_view(), name='Completed-Task'),
    path('add-task-to-user/<int:pk>', AssignTaskToUser.as_view(), name="add-task-to-user"),
    path('complit-task/<int:pk>', CompleteTaskView.as_view(), name="Complete-Task-View"),
    path('add-comment', CommentAddView.as_view(), name="CommentAdd-view"),
    path('comment/<int:pk>', CommentView.as_view(), name="Comment-view"),
]