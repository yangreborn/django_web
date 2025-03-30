from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
from blog.models import CustomUser
from api.serializers import UserSerializer

@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        books = CustomUser.objects.all()
        serializer = UserSerializer(books, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)