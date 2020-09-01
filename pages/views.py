from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from blog.models import Tag, Post
from pages.forms import ContactForm
from pages.models import Contact

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
  if request.method == 'POST':
    contact_form = ContactForm(data=request.POST)
    if contact_form.is_valid():
      name = contact_form.cleaned_data.get('name')
      email = contact_form.cleaned_data.get('email')
      subject = contact_form.cleaned_data.get('subject')
      message = contact_form.cleaned_data.get('message')

      contact_form_message = Contact(name=name, email=email, subject=subject, message=message)
      contact_form_message.save()
      print(settings.ADMIN_EMAIL)
      recipients = [settings.ADMIN_EMAIL]
      send_mail(subject=subject, message=message, from_email=email, recipient_list=recipients)
      messages.info(request, 'Message was sent. we will reach you shortly. Thanks')
      return redirect('pages-contact')
    else:
      messages.warning(request, 'Fill the captcha correctly.')
      # return redirect('pages-contact')
      context = {
        'title': 'Contact Us',
        'tags': Tag.objects.all(),
        'contact_form': contact_form
      }
      return render(request, 'pages/contact.html', context)
  else:
    context = {
        'title': 'Contact Us',
        'tags': Tag.objects.all(),
        'contact_form': ContactForm()
    }
    return render(request, 'pages/contact.html', context)
