from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [ 'pk', 'title', 'price', 'isbn', 'date', 'num_pages' ]
        extra_kwargs = {
            'date' : {'required': False}
        }