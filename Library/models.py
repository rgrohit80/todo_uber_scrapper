from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Page(models.Model):
    book = models.ForeignKey(Book, related_name='related_book', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text
