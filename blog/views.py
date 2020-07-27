from django.shortcuts import render
from .models import Post

# Blog index view.
def index(request):
  context = {
    'title': 'Blog',
    'posts': Post.objects.order_by('date_posted')[::-1]
  }
  return render(request, 'blog/index.html', context)

# Blog detail view
def detail(request, pk):
  post = Post.objects.get(id=pk)
  context = {
      'title': post.title,
      'post': post
  }
  return render(request, 'blog/detail.html', context)

# Blogs by tags view
def get_by_tags(request, tag):
  # if request.method == 'GET' and request.GET['tag']:
  context = {
      'title': f'{tag} Posts',
      'posts': Post.objects.filter(tags__name=tag)
  }
  return render(request, 'blog/index.html', context)
