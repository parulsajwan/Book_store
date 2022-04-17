# ###
# Admin Class for Customer model
# ###

from django.contrib import admin
from store.models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    fieldsets = []
    search_fields = ['name', 'id', 'email']
