from django.shortcuts import render
from rest_framework import generics, status
from .serializers import TodoSerializer

from .models import Todo
# Create your views here.


class TodoListView(generics.ListAPIView):
    model = Todo
    serializer_class = TodoSerializer
    