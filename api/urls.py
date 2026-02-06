from django.urls import path

from api import views

urlpatterns = [
    path('tasks/', views.TasksListView.as_view(), name='tasks_list'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
]