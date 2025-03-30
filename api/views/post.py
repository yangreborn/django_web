from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
from blog.models import Post
from api.serializers import PostSerializer

@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        books = Post.objects.all()
        serializer = PostSerializer(books, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)