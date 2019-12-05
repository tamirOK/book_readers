from rest_framework import serializers

from .models import Book, Reader


class ReaderSerializer(serializers.ModelSerializer):

    books = serializers.StringRelatedField(many=True)

    class Meta:
        model = Reader
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
