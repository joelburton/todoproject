from django.shortcuts import render
from django.views import generic
from todo.models import TodoList


class TodoListListView(generic.ListView):
    model = TodoList


class TodoListDetailView(generic.DetailView):
    model = TodoList