# ###
# Snippet serializers all go here to prevent circular import problems
# ###

from rest_framework import serializers
from store.models import (
    Customer,
    Books,
    )

class CustomerDetailSnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name','email')

class BooksDetailsnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('book_name','description')