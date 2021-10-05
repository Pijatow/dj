from django.shortcuts import render, HttpResponse, get_object_or_404, get_list_or_404
from django.http import Http404
from .models import Author, Post

# Create your views here.


def home_view(request):
    context = {
        'title': 'BLOG',
        'recent_posts': Post.objects.recent_published_posts(5)
    }
    return render(request, 'blog/blog_home.html', context)


def get_authors(request):
    context = {
        'title': 'BLOG',
        'authors': Author.objects.all()
    }
    return render(request, 'blog/authors.html', context)


def get_author_posts(request, author_id):
    # try:
    #     author = Author.objects.get(pk=author_id)
    # except Author.DoesNotExist:
    #     # return HttpResponse('N/A')
    #     raise Http404(f"Author id: {author_id} not found!")
    author = get_object_or_404(Author, pk=author_id)

    context = {
        'title': f'{author.name}\'s posts',
        'author': author,
        'posts': author.get_posts(),
    }
    return render(request, 'blog/author_posts.html', context)
