from django.shortcuts import render, redirect
from blog.models import Tag

# index page
def index(request):
  return redirect('blog-index')

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
