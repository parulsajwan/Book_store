# ###
# Customer view entry points exposed as service methods in the corresponding URL file
# ###

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from store.models import Customer
from store.serializers.CustomerSerializer import (
    CustomerSerializer,
    CustomerBooksCountSerializer,
)


@method_decorator(csrf_exempt, name='dispatch')
class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.get_queryset()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    session_classes = [SessionAuthentication]

@method_decorator(csrf_exempt, name='dispatch')
class CustomerBooksCountRetreiveView(generics.ListAPIView):
    queryset = Customer.objects.get_queryset()
    serializer_class = CustomerBooksCountSerializer
    permission_classes = [IsAuthenticated]
    session_classes = [SessionAuthentication]

@method_decorator(csrf_exempt, name='dispatch')
class CustomerRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Customer.objects.get_queryset()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    session_classes = [SessionAuthentication]
    
    
    