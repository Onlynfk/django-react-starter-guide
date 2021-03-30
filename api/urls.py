from django.urls import path
from .views import TodoListView

urlpatterns = [
    path('todo', TodoListView.as_view()), 
]
