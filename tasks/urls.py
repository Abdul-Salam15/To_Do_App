from django.urls import path
from . import views


app_name = 'tasks'
urlpatterns = [
    path("", views.home, name = "home"),
    path("tasks/<int:pk>/", views.task, name = "tasks"),
    path('update_task/<int:pk>/', views.update_task, name = 'update_task'),
    path('delete_task/<int:pk>/', views.delete_task, name = 'delete_task'),
    path('update_list/<int:pk>/', views.update_list, name = 'update_list'),
    path('delete_list/<int:pk>/', views.delete_list, name = 'delete_list'),

]