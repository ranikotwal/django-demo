from django.shortcuts import render
from rest_framework.views import APIView
from .models import Blog, Book
from .serializers import BlogSerializer
from rest_framework . response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated  # for token
from rest_framework.authentication import TokenAuthentication
from .serializers import BookSerializer

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

class BookListAPIView(APIView):
    serializer_class = BookSerializer

    def get(self , request, *args, **kwargs):
        '''
        Get Book List
        '''
        queryset = Book.objects.all()
        if request.query_params:
            books = Book.objects.filyer(**request.query_params.dict())
        else:
            books = Book.objects.all()

        if books:
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kargs):
        '''
        post bookview data
        '''
        books = BookSerializer(data=request.data)
        if books.is_valid():
            books.save()
            return Response(books.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class BookDetailApiView(APIView):
    serializer_class = BookSerializer

    def get(self, request,pk=None):
        '''get single post
        '''
        if pk:
            try:
                books= Book.objects.get(pk=pk)
            except:
                return response(status=status.HTTP_404_NOT_FOUND)

            if books:
                serializer = BookSerializer(books)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request,pk=None):
        print("111111111")
        '''
        Update Book data
        '''
        book = Book.objects.get(pk=pk)
        data = BookSerializer(instance = book, data=request.data)
        if data.is_valid():
            data.save()
            print("22222222")
            return Response(data.data)
        else:
            print("33333333")
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request,pk=None):
        '''
        delete Book detail
        '''
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


