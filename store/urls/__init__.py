from django.conf.urls import include, url

urlpatterns = [
    url('customer/', include('store.urls.CustomerUrls')),
    url('favbook/', include('store.urls.FavouriteBooksUrls')),
    url('books/', include('store.urls.BooksUrls')),
   ]
