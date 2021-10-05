from .models import Author, Post
from django.db.models import Avg, Max, Min, Sum


def author_objs():
    return Author.objects.all()


def post_objs():
    return Post.objects.all()
