from rest_framework import serializers
from .models import Candidato


class ListaCandidatos(serializer.ModelSeriaLizer):
    class Meta:
        model = Candidato
        fields = ('nome', 'endereco', 'proficao', 'contato')
    


