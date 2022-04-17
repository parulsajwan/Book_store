from django.urls import include, path

urlpatterns = [
    path('customer/', include('store.urls.CustomerUrls')),
    path('favbook/', include('store.urls.FavouriteBooksUrls')),
    path('books/', include('store.urls.BooksUrls')),
   ]
