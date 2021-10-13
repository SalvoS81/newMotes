from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from newMotes.apiMotes.serializers import *
from newMotes.apiMotes.models import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class SequenzaRiposiViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows SequenzaRiposi to be viewed or edited.
    """
    queryset = SequenzaRiposi.objects.all()
    serializer_class = SequenzaRiposiSerializer
    permission_classes = [permissions.IsAuthenticated]

class LavoratoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Lavoratore to be viewed or edited.
    """
    queryset = Lavoratore.objects.all()
    serializer_class = LavoratoreSerializer
    permission_classes = [permissions.IsAuthenticated]

class LineaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Linea to be viewed or edited.
    """
    queryset = Linea.objects.all()
    serializer_class = LineaSerializer
    permission_classes = [permissions.IsAuthenticated]

class TurnoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Turno to be viewed or edited.
    """
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer
    permission_classes = [permissions.IsAuthenticated]

class MatriceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Matrice to be viewed or edited.
    """
    queryset = Matrice.objects.all()
    serializer_class = MatriceSerializer
    permission_classes = [permissions.IsAuthenticated]

class EventoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Evento to be viewed or edited.
    """
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [permissions.IsAuthenticated]