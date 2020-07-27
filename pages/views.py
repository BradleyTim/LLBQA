from django.shortcuts import render, redirect

# index view
# def index(request):
#   context = {
#     'title': 'Home'
#   }
#   return render(request, 'pages/index.html', context)

def index(request):
  return redirect('blog-index')

# about view
def about(request):
  context = {
      'title': 'About Us'
  }
  return render(request, 'pages/about.html', context)

# contact view
def contact(request):
  context = {
      'title': 'Contact Us'
  }
  return render(request, 'pages/contact.html', context)
