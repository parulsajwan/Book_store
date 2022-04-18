# ###
# LikedBook object serializers used in data transformation in store
# ###

from rest_framework import serializers
from store.models import LikedBook

class LikedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikedBook
        fields = '__all__'
