from django.shortcuts import render
from blog.models import Tag, Post

# Blog index view.
def index(request):
  context = {
    'title': 'Blog',
    'posts': Post.objects.order_by('date_posted')[::-1],
    'tags': Tag.objects.all()
  }
  return render(request, 'blog/index.html', context)

# about view
def about(request):
  context = {
      'title': 'About Us',
      'tags': Tag.objects.all()
  }
  return render(request, 'pages/about.html', context)

# contact view
def contact(request):
  context = {
      'title': 'Contact Us',
      'tags': Tag.objects.all()
  }
  return render(request, 'pages/contact.html', context)
