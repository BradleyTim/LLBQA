from django.db import models
from django.utils import timezone

# contact form model
class Contact(models.Model):
  name = models.CharField(max_length=140)
  email = models.EmailField()
  subject = models.CharField(max_length=140)
  message = models.TextField()
  created_at = models.DateField(default=timezone.now)
  read = models.BooleanField(default=False)

  def __str__(self):
    return f'contact message from {self.name}, {self.email}'
