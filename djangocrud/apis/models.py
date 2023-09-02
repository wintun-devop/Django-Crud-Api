from pyexpat import model
from django.db import models
import uuid

# Create your models here.

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=200,unique=True)
    price = models.FloatField()
    quantity = models.PositiveIntegerField()
