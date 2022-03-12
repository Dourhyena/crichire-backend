from django.shortcuts import render
from .models import Player, Player_Stats, Fixture, CompletePlayer
from .serializers import Player_StatsSerializer, PlayerSerializer, FixtureSerializer, CompletePlayerSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class PlayerViewSet(viewsets.ModelViewSet):

    # permission_classes = [IsAuthenticated]
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class Player_StatsViewSet(viewsets.ModelViewSet):

    # permission_classes = [IsAuthenticated]
    queryset = Player_Stats.objects.all()
    serializer_class = Player_StatsSerializer

class FixtureViewSet(viewsets.ModelViewSet):

    # permission_classes = []
    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer


class CompletePlayerViewset(viewsets.ModelViewSet):
    queryset = CompletePlayer.objects.raw('CALL Jointables()')
    serializer_class = CompletePlayerSerializer





