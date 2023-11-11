from rest_framework.serializers import ModelSerializer

from reserva.models import Reserva, CategoriaAnimal

class ReservaModelSerializer(ModelSerializer):
    class Meta:
        model = Reserva
        '''fields = [
            'id',
            'nome',
            'email',
            'nome_pet',
            'data',
            'turno',
            'categoria_animal',
            'observacoes',
            'banho_conclusao'
        ]'''
        fields = '__all__'


class CategoriaAnimalModelSerializer(ModelSerializer):
    class Meta:
        model = CategoriaAnimal
        fields = '__all__'
