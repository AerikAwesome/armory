from django.db import models

# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=100)
    author_pic = models.ImageField
    def __str__(self):
        return self.author_name

class Post(models.Model):
    post_author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    post_title = models.CharField(max_length=200)
    post_text = models.TextField
    post_date = models.DateTimeField('date published')
    def __str__(self):
        return self.post_title

class Comment(models.Model):
    com_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    com_text = models.TextField(max_length=300)
    com_date = models.DateTimeField('date commented')
    def __str__(self):
        return self.com_text