from .models import Training
from rest_framework import serializers

class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(TrainingSerializer, self).to_representation(instance)
        rep['player'] = instance.player.name
        return rep
