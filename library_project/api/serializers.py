from rest_framework import serializers
from api.models import Book, CheckOut, BookStatus
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """A Book Serializer"""

    class Meta:
        model = Book
        fields = ['author', 'title', 'ISBN', 'published_date', 'book_copies']

    
    # def validate_ISBN(self, value):
    #     pass

    # def validate_book_copies(self, value):
    #     pass
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    def validate(self, attrs):
        return super().validate(attrs)
    
class BookStatusSerializer(serializers.ModelSerializer):
    """
    The Serializer for setting a book checkout status
    """
    title = serializers.ReadOnlyField(source='book.title')
    author = serializers.ReadOnlyField(source='book.author')
    ISBN = serializers.ReadOnlyField(source='book.ISBN')
    copies_left = serializers.ReadOnlyField(source='book.book_copies')
    class Meta:
        model = BookStatus
        fields = ['status','book', 'title', 'author', 'ISBN', 'copies_left']
    
class CheckOutSerializer(serializers.ModelSerializer):
    book_title = serializers.ReadOnlyField(source='book.book.title')
    username = serializers.ReadOnlyField(source='user.username')
    checkout_date = serializers.ReadOnlyField()
    class Meta:
        model = CheckOut
        fields = ['book', 'user', 'book_title', 'username', 'checkout_date', 'return_date' ]

    def checkout(self, value):
        pass

    # def get_borrower(self, value):
    #     return self.user.username