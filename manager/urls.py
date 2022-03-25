from django.urls import path, include
from .views import UsersListView, CreateTaskView, TaskView, TaskDetailView, MyTaskView, CompletedTaskView, AssignTokenToUser, ComplitTaskView

urlpatterns = [
    path('userslist', UsersListView.as_view(), name='UsersList_list'),
    path('taskcreate', CreateTaskView.as_view(), name='CreateTaskView'),
    path('task', TaskView.as_view(), name='CreateTaskView'),
    path('taskdetail/<int:pk>', TaskDetailView.as_view(), name='TaskdetailView'),
    path('mytask/', MyTaskView.as_view(), name='MyTaskView'),
    path('compited-task', CompletedTaskView.as_view(), name='Complited-Task'),
    path('add-task-to-user/<int:pk>', AssignTokenToUser.as_view(), name="add-task-to-user"),
    path('complit-task',ComplitTaskView.as_view(), name="ComplitTaskView"),
]