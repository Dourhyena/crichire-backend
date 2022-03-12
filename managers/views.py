from .models import Manager
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ManagerSerializer



class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer



