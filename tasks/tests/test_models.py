"""
    Unit test file for models
"""
from django.test import TestCase

from tasks.models import Task


class TaskModelTest(TestCase):
    """
    Test Model class
    """
    @classmethod
    def setUpTestData(cls):
        """
        :return: None
        """
        # Setting up objects which can be use for all test methods
        Task.objects.create(task_title='Development', task_description='This task includes all the development '
                                                                       'related activities for this project')

    def test_task_title_field_label(self):
        """
        :return: None
        """
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('task_title').verbose_name
        self.assertEqual(field_label, 'Task Title')

    def test_task_description_field_label(self):
        """
        :return: None
        """
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('task_description').verbose_name
        self.assertEqual(field_label, 'Task Description')

    def test_get_absolute_url(self):
        """
        :return: None
        """
        task = Task.objects.get(id=1)
        self.assertEqual(task.get_absolute_url(), '/edit/1')

    def test_auto_update_datetime(self):
        """
        :return: None
        """
        # fetch object from db and capture modified_date
        task = Task.objects.get(id=1)
        old_modified_date = task.task_updated

        # set new title
        task.task_title = 'some other title'
        task.save()

        # re-fetch object from db
        task.refresh_from_db()
        new_modified_date = task.task_updated

        # assert auto update filed functionality
        self.assertGreater(new_modified_date, old_modified_date)

    def test_can_save_same_task_title(self):
        t1 = Task.objects.create(task_title='same-name')
        t2 = Task.objects.create(task_title='same-name')
        self.assertEqual(t1.task_title, t2.task_title)
