from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django_markdown.models import MarkdownField
from taggit.managers import TaggableManager

# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=100, default='anonymous')
    author_thumbnail = ProcessedImageField(upload_to='avatars',
                                           processors=[ResizeToFill(100,50)],format='JPEG',
                                           options={'quality': 60},
                                           default='settings.MEDIA_ROOT/avatars/default.jpg')
    def __str__(self):
        return self.author_name

class Post(models.Model):
    post_author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    post_title = models.CharField(max_length=200, default='A title here')
    post_text = MarkdownField(default='Some text here.')
    post_date = models.DateTimeField('date published')
    tags = TaggableManager()
    def __str__(self):
        return self.post_title
    pass

class Comment(models.Model):
    com_post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    com_author = models.CharField(max_length=100, default='Anonymous')
    com_text = models.TextField(max_length=300, default='')
    com_date = models.DateTimeField('date commented')
    def __str__(self):
        return self.com_text