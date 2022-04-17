# ###
# URL patterns for Books
# ###

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.cache import cache_page

from store.views import BooksView as v

#for  Books
urlpatterns = [
    path('create/',v.BooksCreateView.as_view()),
    path('<int:pk>/',v.BooksRetrieveUpdateView.as_view()),
    path('',cache_page(60*10)(v.BooksListView.as_view())),
]
urlpatterns = format_suffix_patterns(urlpatterns)
