from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
class Tareas(models.Model):
    STATUS_CHOICES = (
        ("TODO", "Todo"),
        ("INPROGRESS", "In Progress"),
        ("DONE", "Done"),
        ("CLOSE", "Close"),
    )


    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=300)
    completada = models.BooleanField(default=False)
    status = models.CharField(max_length=10,
                    choices=STATUS_CHOICES,
                    default="TODO")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    vencimiento = models.DateTimeField(auto_now=False, auto_now_add=False, null = True, blank = True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre


