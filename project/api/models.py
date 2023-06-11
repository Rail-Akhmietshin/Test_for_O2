from django.db import models
from .utils import get_random_name


# Create your models here.

class Post(models.Model):
    name = models.CharField(default=get_random_name)


class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    postId = models.ForeignKey(Post, on_delete=models.PROTECT)
