from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField

# Tags model
class Tag(models.Model):
  name = models.CharField(max_length=140)

  def __str__(self):
    return self.name

# Post model
class Post(models.Model):
  title = models.CharField(max_length=200)
  slug = models.CharField(max_length=200, unique=True)
  summary = models.CharField(max_length=200, blank=True)
  content = models.TextField()
  date_posted = models.DateField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  tags = models.ManyToManyField(Tag)

  def __str__(self):
    return self.title
