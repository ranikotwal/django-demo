from django.urls import path
from .import views
from .views import BlogListAPIView, BlogDetailApiView , BookListAPIView, BookDetailApiView

urlpatterns = [
    path('blog/', BlogListAPIView.as_view(), name='blog-list-Api'),
    path('blog/<int:pk>',BlogDetailApiView.as_view()),

    #for book
    path('book/', BookListAPIView.as_view(), name='book-list-Api'),
    path('book/<int:pk>',BookDetailApiView.as_view()),
]