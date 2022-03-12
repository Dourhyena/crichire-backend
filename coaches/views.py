from .models import Training
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import TrainingSerializer



class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
