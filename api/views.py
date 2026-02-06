
from django.shortcuts import render
from rest_framework import generics

from api.models import Task
from api.serializers import TasksSerializer


# Create your views here.
class TasksListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset


class TaskDetailView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer