from django.contrib.auth.models import User, Group
from rest_framework import serializers
from newMotes.apiMotes.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class SequenzaRiposiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SequenzaRiposi
        fields = ['nome', 'sequenza']


class LavoratoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lavoratore
        fields = ['matricola', 'nominativo', 'mansione', 'sequenza_riposi', 'data_per_sequenza', 'indice_per_sequenza']


class LineaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Linea
        fields = ['nome', 'polo', 'descrizione']


class TurnoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Turno
        fields = ['mansione', 'priorita', 'linea', 'polo_monta', 'fascia', 'ora_inizio', 'ora_fine', 'note']


class MatriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Matrice
        fields = ['data', 'nome', 'turni']


class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = ['data', 'lavoratore', 'tipologia', 'turno']


