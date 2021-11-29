from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TaskList.as_view(), name='tasks_list'),
    path('new/', views.TaskCreate.as_view(), name='tasks_new'),
    path('task/<int:pk>', views.TaskDetails.as_view(), name='tasks_view'),
    path('task/', views.task_default, name='default_task'),
    path('edit/<int:pk>', views.TaskUpdate.as_view(), name='tasks_edit'),
    path('delete/<int:pk>', views.TaskDelete.as_view(), name='tasks_delete'),
    path('fake/', views.fake_view, name='fake_view'),
]
