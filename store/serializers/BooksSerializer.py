# ###
# Books object serializers used in data transformation in store
# ###

from rest_framework import serializers
from store.models import Books

class BooksSerializer(serializers.ModelSerializer):
    image_link = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Books
        fields = '__all__'
