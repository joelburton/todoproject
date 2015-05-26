from django.test import TestCase
from todo.models import TodoList, TodoItem


class TestTodoList(TestCase):
    def test_is_complete(self):
        my_list = TodoList.objects.create(name='Work Stuff')
        item1 = TodoItem.objects.create(todolist=my_list, name='Clean desk')
        item2 = TodoItem.objects.create(todolist=my_list, name='Hire Balloonicorn', done=True)

        self.assertFalse(my_list.is_done())

        item1.done = True
        item1.save()

        self.assertTrue(my_list.is_done())

