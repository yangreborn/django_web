from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
from blog.models import Books
from api.serializers import BooksSerializer
from django.core.cache import cache
import uuid

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Books.objects.all()
        serializer = BooksSerializer(books, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def book_details(request, id):
    try:
        books = Books.objects.get(id=id)
    except Books.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        qr_id = str(uuid.uuid4())
        cache_key = f'qr_code_{qr_id}'
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)
        serializer = BooksSerializer(books)
        cache.set(cache_key, serializer.data, timeout=300)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = BooksSerializer(books, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)