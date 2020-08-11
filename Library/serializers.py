from rest_framework import serializers
from .models import Page, Book


class PageSerializer(serializers.Serializer):
    class Meta:
        model = Page
        fields = "__all__"


class BookSerializer(serializers.Serializer):
    page = PageSerializer(many=True)
    title = serializers.CharField(max_length=50)

    class Meta:
        model = Book
        fields = ['title', 'page']

    # def create(self, validated_data):
    #     # Create the book instance
    #     book = Book.objects.create(title=validated_data['title'])
    #
    #     # Create or update each page instance
    #     for item in validated_data['pages']:
    #         page = Page(id=item['page_id'], text=item['text'], book=book)
    #         page.save()
    #
    #     return book
