from django.forms import ModelForm
from .models import Contact

# contact form
class ContactForm(ModelForm):
  class Meta:
    model = Contact
    fields = ['name', 'email', 'subject', 'message']
