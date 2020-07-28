from django.shortcuts import render, get_object_or_404
from .models import Post, Tag

# Blog index view.
def index(request):
  context = {
    'title': 'Blog',
    'posts': Post.objects.order_by('date_posted')[::-1],
    'tags': Tag.objects.all()
  }
  return render(request, 'blog/index.html', context)

# Blog detail view
def detail(request, pk, slug):
  # post = Post.objects.get(slug=slug)
  post = get_object_or_404(Post, id=pk, slug=slug)
  context = {
      'title': post.title,
      'post': post,
      'tags': Tag.objects.all()
  }
  return render(request, 'blog/detail.html', context)

# Blogs by tags view
def get_by_tags(request, tag):
  context = {
      'title': f'{tag} Posts',
      'posts': Post.objects.filter(tags__name=tag),
      'tags': Tag.objects.all()
  }
  return render(request, 'blog/index.html', context)
