from django.forms import ModelForm, TextInput, Textarea
from captcha.fields import CaptchaField
from .models import Contact

# contact form
class ContactForm(ModelForm):
  captcha = CaptchaField()

  class Meta:
    model = Contact
    fields = ['name', 'email', 'subject', 'message']
    widgets = {
      'name': TextInput(attrs={'placeholder': 'Name'}),
      'email': TextInput(attrs={'placeholder': 'email@example.com'}),
      'subject': TextInput(attrs={'placeholder': 'Subject/Topic'}),
      'message': Textarea(attrs={'placeholder': 'Your message here..'}),
    }    
