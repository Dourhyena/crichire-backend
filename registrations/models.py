from django.db import models
from managers.models import Manager

class Registration(models.Model):
    STATUS = [
                ('APR', 'approved'),
                ('PND', 'pending'),
                ('RJT', 'rejected')
    ] 
    name = models.CharField(max_length=50)
    dob = models.DateField()
    achievements = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    pno = models.PositiveIntegerField()
    education = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    status = models.CharField(choices=STATUS, max_length=10, default='PND')
    m = models.ForeignKey(Manager, on_delete=models.CASCADE, default=1)