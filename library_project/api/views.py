from django.shortcuts import render
from django.core import serializers as django_serializer
from django.utils import timezone
from django.forms.models import model_to_dict
import json

from api.serializers import BookSerializer, BookStatusSerializer, CheckOutSerializer
from api.models import Book, BookStatus, CheckOut

from rest_framework import generics, views, viewsets
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action

from django_filters import filters

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        # book = self.get_object()
        # book_stat = BookStatus.objects.get(book=book)
        # book_stat.update_checkout_status()
        # print('Book Status Changed')
        return super().update(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    @action(detail=True, methods=['post','get'], url_path='checkout')
    def checkout_book(self, request, *args, pk=None, **kwargs):
        book = Book.objects.get(id=pk)
        book_status = BookStatus.objects.get(book=book)
        print(f"{book.title} {book_status.status}")
        user = request.user
        print(user.username)
        request.data['user'] = user.id
        request.data['book'] = book_status.id
        serializer = CheckOutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete','get'], url_path='return')
    def return_book(self, request, *args,pk=None, **kwargs):
        book = Book.objects.get(id=pk)
        book_status = BookStatus.objects.get(book=book)
        user = request.user
        request.data['user'] = user.id
        request.data['book'] = book_status.id

        checked_out_book = CheckOut.objects.get(book=book_status, user=user)
        dict_obj = model_to_dict(checked_out_book)
        serializer = json.dumps(dict_obj)
        if serializer:
            if user == checked_out_book.user:
                checked_out_book.return_date = timezone.now()
                checked_out_book.save()
                checked_out_book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT, data=serializer)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get_permissions(self):
        return super().get_permissions()
    
class AvailableBooks(viewsets.ReadOnlyModelViewSet):
    serializer_class = BookStatusSerializer
    queryset = BookStatus.objects.all().filter(status=1)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = []