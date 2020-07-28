from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Tag

# Register your models here.
class PostAdmin(SummernoteModelAdmin):
  list_display = ('title', 'slug', 'author','date_posted')
  list_filter = ('title', 'date_posted')
  search_fields = ['title', 'slug']
  prepopulated_fields = {'slug': ('title',)}
  summernote_fields = ('content',)
  
admin.site.register(Post, PostAdmin)

class TagAdmin(admin.ModelAdmin):
  list_display = ('name',)
  list_filter = ('name',)
  search_fields = ['name',]

admin.site.register(Tag, TagAdmin)
