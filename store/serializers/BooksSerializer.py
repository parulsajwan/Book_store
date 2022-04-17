# ###
# Books object serializers used in data transformation in store
# ###

from rest_framework import serializers
from store.models import Books

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
