from rest_framework import serializers

from web.models import Reader, Book


class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = {'firstname','lastname','date_of_birth'}

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = {'title','genre'}

class BorrowSerializer(serializers.Serializer):
    reader = ReaderSerializer()
    book = BookSerializer()
    borrow_date = serializers.DateTimeField()
    return_date = serializers.DateTimeField()