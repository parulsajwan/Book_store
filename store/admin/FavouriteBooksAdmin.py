# ###
# Admin Class for FavouriteBooks model
# ###

from django.contrib import admin
from store.models import FavouriteBooks

# Register your models here.
class FavouriteBooksAdmin(admin.ModelAdmin):
    model = FavouriteBooks
    fieldsets = []
    search_fields = ['id']
