from django.db import models
from django.utils import timezone # no usada
from django.contrib.auth.models import User

# Create your models here.
class Trailer(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    titulo = models.CharField(max_length=150)
    descripcion=models.TextField()
    link=models.TextField()
    texto = models.TextField()
    class Meta:
        ordering = ('-titulo',)
    def __str__(self):
        return self.titulo