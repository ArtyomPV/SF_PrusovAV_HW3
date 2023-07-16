from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Author(models.Model):
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)


class Post(models.Model):
    NEWS = 'NW'
    POST = 'PT'
    POSTS =[
        (NEWS, 'news'),
        (POST, 'post')
    ]
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=2, choices=POSTS, default=NEWS)
    data_post_creation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating_post = models.IntegerField(default=0)
    category = models.ManyToManyField(Category, through='PostCategory')


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_comment = models.ForeignKey(User, on_delete=models.CASCADE)
    rating_comment = models.IntegerField(default=0)
    text_comment = models.TextField()
    data_comment_creation = models.DateTimeField(auto_now_add=True)
