
from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from api.models import Task
from api.serializers import TasksSerializer


# Create your views here.
class TasksListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['id', 'title']

    def get_queryset(self):
        queryset = Task.objects.all()
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset


class TaskDetailView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer