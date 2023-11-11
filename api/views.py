from rest_framework.viewsets import ModelViewSet
from reserva.models import Reserva, CategoriaAnimal
from api.serializers import ReservaModelSerializer, CategoriaAnimalModelSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ReservaModelViewSet(ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CategoriaAnimalModelViewSet(ModelViewSet):
    queryset = CategoriaAnimal.objects.all()
    serializer_class = CategoriaAnimalModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]