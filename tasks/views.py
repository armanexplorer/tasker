"""
Task app: Views file
"""
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponse
# from django.shortcuts import redirect

from tasks.models import Task


class TaskList(ListView):
    """
    Task list Generic List View
    """
    model = Task

    def get_context_data(self, **kwargs):
        context = super(TaskList, self).get_context_data(**kwargs)
        context.update({'nlink': 'list'})
        return context


class TaskCreate(CreateView, ListView):
    """
    Task list Generic Create View
    """
    object_list = Task.objects.all()
    model = Task
    fields = ['task_title', 'task_description']
    success_url = reverse_lazy('tasks:tasks_list')

    def get_context_data(self, **kwargs):
        context = super(TaskCreate, self).get_context_data(**kwargs)
        context.update({'nlink': 'new'})
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['task_title'].required = True
        return form


class TaskDetails(DetailView, ListView):
    """
    Task list Detail View
    """
    object_list = Task.objects.all()
    model = Task
    fields = ['task_title', 'task_description', 'task_created', 'task_updated']


class TaskUpdate(UpdateView, ListView):
    """
    Task list Update View
    """
    object_list = Task.objects.all()
    model = Task
    fields = ['task_title', 'task_description']
    success_url = reverse_lazy('tasks:tasks_list')

    def get_context_data(self, **kwargs):
        context = super(TaskUpdate, self).get_context_data(**kwargs)
        context.update({'nlink': 'update'})
        return context


class TaskDelete(DeleteView, ListView):
    """
    Task list Delete View
    """
    object_list = Task.objects.all()
    model = Task
    success_url = reverse_lazy('tasks:tasks_list')


def task_default(request):
    """
    this is default behaviour when there is no id
    """
    return TaskDetails.as_view()(request, pk=Task.objects.first().pk)


class Custom404(TemplateView):
    """
    Task list Custom 404 View
    """
    template_name = 'tasks/404.html'


class Custom500(TemplateView):
    """
    Task list Custom 500 View
    """
    template_name = 'tasks/500.html'


def fake_view(request):
    from django.core.cache import cache
    cache.set('key', 1)
    return HttpResponse(cache.get('key'))
