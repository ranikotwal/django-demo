from django.urls import path
from .import views
from .views import BlogListAPIView, BlogDetailApiView

urlpatterns = [
    path('blog/', BlogListAPIView.as_view(), name='blog-list-Api'),
    path('blog/<int:pk>',BlogDetailApiView.as_view()),
]