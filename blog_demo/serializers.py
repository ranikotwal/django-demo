from rest_framework import serializers
from . models import Blog, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name','title']



class BlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)
    class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'content','image']

