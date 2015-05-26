from django.contrib import admin
from todo.models import TodoList, TodoItem

class TodoItemsInline(admin.TabularInline):
    model = TodoItem
    extra = 1

class TodoListAdmin(admin.ModelAdmin):
    inlines = [TodoItemsInline]

admin.site.register(TodoList, TodoListAdmin)
admin.site.register(TodoItem)
