from .views import TaskListCreateAPIView, TaskGetUpdateDelete
from django.urls import path
template_name = {'template_name': 'rest_framework/login.html'}
from django.contrib.auth import views


urlpatterns = [
    path('', TaskListCreateAPIView.as_view(), name='task'),
    path('<int:pk>', TaskGetUpdateDelete.as_view(), name='Task_Details'),
]
