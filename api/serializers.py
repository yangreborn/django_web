from rest_framework import serializers
from blog.models import Post, Category, Tag, Comment, CustomUser, Books
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = '__all__'
        
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # 增加想要加到token中的信息
        token['username'] = user.username
        token['email'] = user.email
        # ...
        return token
    
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'