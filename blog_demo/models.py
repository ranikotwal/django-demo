from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image= models.FileField(null=True)

class Author(models.Model):
    name=models.CharField   (max_length=100)
    title= models.ForeignKey(Blog, on_delete= models.CASCADE, related_name='author')

    def __str__(self):
        return self.name

