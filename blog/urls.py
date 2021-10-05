from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='blog-home'),
    path('author/', views.get_authors),
    path('author/<int:author_id>/', views.get_author_posts),
]
