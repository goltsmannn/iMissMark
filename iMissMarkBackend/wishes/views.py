from rest_framework import permissions, viewsets

from .models import Wish
from .serializers import UserSerializer, WishSerializer

class WishViewSet(viewsets.ModelViewSet):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer