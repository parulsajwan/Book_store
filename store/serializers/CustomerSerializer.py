# ###
# Customer object serializers used in data transformation in store
# ###
from django.contrib.auth.hashers import make_password
from store.models import FavouriteBooks
from store.models import Customer
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'
        
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(CustomerSerializer, self).create(validated_data)
    
class CustomerBooksCountSerializer(serializers.ModelSerializer):
    class Favouritebook(serializers.ModelSerializer):
        
        def to_representation(self, instance):
            representation = super().to_representation(instance) 
            representation['book_count'] = instance.favourite_books_list.count()
            return representation
        
        class Meta:
            model=FavouriteBooks
            fields = ['id']

    favoriteBooks = Favouritebook(many=True,source ='favouritebooks_set')
    class Meta:
        model = Customer
        fields = ['favoriteBooks','id','name','email','password']
    
        
    
