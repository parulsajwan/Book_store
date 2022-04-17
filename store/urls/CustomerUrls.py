# ###
# URL patterns for Customer
# ###

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from store.views import CustomerView as v

#for  Customer
urlpatterns = [
    path('',v.CustomerListCreateView.as_view()),
    path('<int:pk>/',v.CustomerRetrieveUpdateView.as_view()),
    path('bookcount/',v.CustomerBooksCountRetreiveView.as_view()),
    
]
urlpatterns = format_suffix_patterns(urlpatterns)
