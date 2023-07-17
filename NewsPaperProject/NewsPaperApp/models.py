from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum


class Author(models.Model):
    author_name = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        postRat = self.post_set.all().aggregate(posting=Sum('rating_post'))
        prat = 0
        prat += postRat.get('posting')
        self.rating = prat
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)


class Post(models.Model):
    NEWS = 'NW'
    POST = 'PT'
    POSTS = [
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

    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post -= 1
        self.save()

    def preview(self):
        return self.text[0:123] + '...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_comment = models.ForeignKey(User, on_delete=models.CASCADE)
    rating_comment = models.IntegerField(default=0)
    text_comment = models.TextField()
    data_comment_creation = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.author_comment.username

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()
