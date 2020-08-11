from django.shortcuts import render

# Create your views here.
from .serializers import BookSerializer, PageSerializer
from .models import Book, Page
from rest_framework import generics


class BookListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
