from .views import BookListCreateAPIView
from django.urls import path

urlpatterns = [
    path('', BookListCreateAPIView.as_view()),
]
