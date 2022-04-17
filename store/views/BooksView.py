# ###
# Books view entry points exposed as service methods in the corresponding URL file
# ###

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response

from store.models import Books
from store.serializers.BooksSerializer import BooksSerializer

@method_decorator(csrf_exempt, name='dispatch')
class BooksListView(generics.ListAPIView):
    queryset = Books.objects.get_queryset()
    serializer_class = BooksSerializer
    permission_classes = [IsAuthenticated]
    session_classes = [SessionAuthentication]

@method_decorator(csrf_exempt, name='dispatch')
class BooksCreateView(generics.CreateAPIView):
    queryset = Books.objects.get_queryset()
    serializer_class = BooksSerializer
    permission_classes = [IsAuthenticated]
    session_classes = [SessionAuthentication]

@method_decorator(csrf_exempt, name='dispatch')
class BooksRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Books.objects.get_queryset()
    serializer_class = BooksSerializer
    permission_classes = [IsAuthenticated]
    session_classes = [SessionAuthentication]