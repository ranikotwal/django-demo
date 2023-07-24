from django.shortcuts import render
from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogSerializer
from rest_framework . response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class BlogListAPIView(APIView):
    serializer_class = BlogSerializer
    # queryset = BlogPost.objects.all()

    def get(self , request, *args, **kargs):
        '''
        Get BlogPost List
        '''
        queryset = Blog.objects.all()
        if request.query_params:
            blogs= Blog.objects.filter(**request.query_params.dict())
        else:
            blogs = Blog.objects.all()

        if blogs:
            serializer = BlogSerializer(blogs, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def post(self, request, *args, **kargs):
        '''
        post blogview data
        '''
        data = {}
        blogs = BlogSerializer(data=request.data)
        if blogs.is_valid():
            blogs.save()
            return Response(blogs.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class BlogDetailApiView(APIView):
    serializer_class = BlogSerializer
    
    def get(self, request, pk=None):
        '''
        get single blog
        '''
        if pk:
            try:
                blog = Blog.objects.get(pk=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

            if blog:
                serializer = BlogSerializer(blog)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)

        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None):
        '''
        Update blog
        '''
        blog = Blog.objects.get(pk=pk)
        data = BlogSerializer(instance=blog, data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        '''
        delete blog
        '''
        blog = get_object_or_404(Blog, pk=pk)
        blog.delete()
        return Response(status=status.HTTP_202_ACCEPTED)






