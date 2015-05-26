from django.db import models

class TodoList(models.Model):
    """A todo list."""

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        foozle = self.name
        return foozle

    def is_done(self):
        """Are all items on our todo list done?"""

        for item in self.todoitem_set.all():
            if not item.done:
                return False
        return True


class TodoItem(models.Model):
    """A single todo item."""

    todolist = models.ForeignKey(TodoList)
    name = models.CharField(max_length=50)
    description = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name








