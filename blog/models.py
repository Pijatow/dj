from django.db import models
from django.utils.timezone import now

# Create your models here.


class AuthorManager(models.Manager):
    pass


class Author(models.Model):
    def __str__(self):
        return f'Name: {self.name} | Email: {self.email}'

    def get_posts(self):
        return self.posts.all()

    name = models.CharField(max_length=40)
    email = models.EmailField()
    objects = AuthorManager()


class PostManager(models.Manager):
    def recent_published_posts(self, count):
        return self.order_by('-pub_date')[:count]


class Post(models.Model):
    def __str__(self):
        return f'Author: {self.author.name}, Topic: {self.topic}'
    topic = models.CharField(max_length=30)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    objects = PostManager()
