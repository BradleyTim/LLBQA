from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
  list_display = ('name', 'email', 'created_at', 'read')
  list_filter = ('name', 'email', 'read')
  search_fields = ['name', 'email']

admin.site.register(Contact, ContactAdmin)