# ###
# Admin Class for Books model
# ###

from django.contrib import admin
from store.models import Books

# Register your models here.
class BooksAdmin(admin.ModelAdmin):
    model = Books
    fieldsets = []
    search_fields = ['name', 'id', 'email']
