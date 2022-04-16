# ###
# URL patterns for FavouriteBooks
# ###

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from store.views import FavouriteBooksView as v

#for  FavouriteBook
urlpatterns = [
    url('',v.FavouriteBooksListCreateView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
