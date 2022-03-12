from .models import Player, Player_Stats, Fixture, CompletePlayer
from rest_framework import serializers



class Player_StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player_Stats
        fields = ['player', 'match_type', 'strike_rate', 'wickets', 'runs', 'is_available', 'economy']


class PlayerSerializer(serializers.ModelSerializer):
    stats = Player_StatsSerializer(many=True)

    class Meta:
        model = Player
        fields = ['jersey', 'name', 'role', 'stats']





class FixtureSerializer(serializers.ModelSerializer):
    model = Fixture
    class Meta:
        model = Fixture
        fields = "__all__"

class CompletePlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletePlayer
        fields = "__all__"

