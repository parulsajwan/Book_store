# ###
# URL patterns for Books
# ###

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from store.views import BooksView as v

#for  Books
urlpatterns = [
    url('',v.BooksListCreateView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
