# ###
# FavouriteBooks view entry points exposed as service methods in the corresponding URL file
# ###

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


from store.models import FavouriteBooks
from store.serializers.FavouriteBooksSerializer import FavouriteBooksSerializer

@method_decorator(csrf_exempt, name='dispatch')
class FavouriteBooksListCreateView(generics.ListCreateAPIView):
    queryset = FavouriteBooks.objects.get_queryset()
    serializer_class = FavouriteBooksSerializer
    permission_classes = [IsAuthenticated]
    session_classes = [SessionAuthentication]

@method_decorator(csrf_exempt, name='dispatch')
class FavouriteBookRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = FavouriteBooks.objects.get_queryset()
    serializer_class = FavouriteBooksSerializer
    permission_classes = [IsAuthenticated]
    session_classes = [SessionAuthentication]

    