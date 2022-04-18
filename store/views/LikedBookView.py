# ###
# LikedBook view entry points exposed as service methods in the corresponding URL file
# ###

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


from store.models import LikedBook
from store.serializers.LikedBookSerializer import LikedBookSerializer

@method_decorator(csrf_exempt, name='dispatch')
class LikedBookListCreateView(generics.ListCreateAPIView):
    queryset = LikedBook.objects.get_queryset()
    serializer_class = LikedBookSerializer
    permission_classes = [IsAuthenticated]
    session_classes = [SessionAuthentication]
