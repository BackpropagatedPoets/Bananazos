from django.db import models
from django.utils import timezone # no usada
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.
class Trailer(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    fecha_salida = models.DateField(auto_created=True,auto_now_add=True)
    vistas = models.PositiveIntegerField(auto_created=True)

    titulo = models.CharField(max_length=100)
    link_video = models.CharField(max_length=400)
    link_imagen = models.CharField(max_length=400)
    duracion = models.CharField(max_length=10, default="0:00")

    
    class Meta:
        ordering = ('-fecha_salida',)
    def __str__(self):
        return str(self.id) + " " + self.titulo


class TrailerForm(ModelForm):
    class Meta:
        model = Trailer
        fields = ['titulo', 'link_video', 'link_imagen', 'duracion']


