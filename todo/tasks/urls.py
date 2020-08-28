from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>/', views.delete, name='delete'),
    path('<int:task_id>/toggle_complete', views.toggle_complete, name='complete'),
    path('/', views.add_task, name='add_task'),
]