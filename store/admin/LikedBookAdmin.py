# ###
# Admin Class for LikedBook model
# ###

from django.contrib import admin
from store.models import LikedBook

# Register your models here.
class LikedBookAdmin(admin.ModelAdmin):
    model = LikedBook
    fieldsets = []
    search_fields = ['id']
