from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.task_create, name='create_task'),
    path('task/<int:pk>', views.task_detail, name='detail_task'),
    path('delete/<int:pk>/', views.task_delete, name='delete_task'),
    path('update/<int:pk>', views.task_update, name='update_task'),
]
