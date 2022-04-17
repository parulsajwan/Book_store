# ###
# URL patterns for FavouriteBooks
# ###

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from store.views import FavouriteBooksView as v

# for  FavouriteBook
urlpatterns = [
    path('',v.FavouriteBooksListCreateView.as_view()),
    path('<int:pk>/',v.FavouriteBookRetrieveUpdateView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
