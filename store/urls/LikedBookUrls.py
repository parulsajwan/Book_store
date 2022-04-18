# ###
# URL patterns for LikedBooks
# ###

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from store.views import LikedBookView as v

# for  LikedBook
urlpatterns = [
    path('',v.LikedBookListCreateView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
