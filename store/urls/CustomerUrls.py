# ###
# URL patterns for Customer
# ###

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from store.views import CustomerView as v

#for  Customer
urlpatterns = [
    url('bookcount/',v.CustomerBooksCountRetreiveView.as_view()),
    url('',v.CustomerListCreateView.as_view()),
    
]
urlpatterns = format_suffix_patterns(urlpatterns)
