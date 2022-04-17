# ###
# FavouriteBooks object serializers used in data transformation in store
# ###

from rest_framework import serializers
from store.models import Books, Customer, FavouriteBooks
from . import SnippetSerializer as snip

class FavouriteBooksDetailSerializer(serializers.ModelSerializer):
    
    customer_id = snip.CustomerDetailSnippetSerializer()
    favourite_books_list = snip.BooksDetailsnippetSerializer(many=True)
    
    class Meta:
        model = FavouriteBooks
        fields = '__all__'

class FavouriteBooksSerializer(serializers.ModelSerializer):   
    class Meta:
        model = FavouriteBooks
        fields = '__all__'