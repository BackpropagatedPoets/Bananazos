from django.db import models
from django.utils import timezone # no usada
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.
class Trailer(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    fecha_salida = models.DateField(auto_created=True,auto_now_add=True)
    vistas = models.PositiveIntegerField(auto_created=True, default=0)
    likes = models.PositiveIntegerField(auto_created=True, default=0)
    dislikes = models.PositiveIntegerField(auto_created=True, default=0)

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

class Comentario(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    trailer_id = models.ForeignKey(Trailer, on_delete=models.CASCADE)
    usuario_username = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(max_length=500, default="")
    class Meta:
        ordering = ('-id',)
    def __str__(self):
        return str(self.usuario_username) + ": " + str(self.trailer_id)

class Reaccion(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    trailer_id = models.ForeignKey(Trailer, on_delete=models.CASCADE)
    usuario_username = models.ForeignKey(User, on_delete=models.CASCADE)
    reaccion = models.ImageField()
    class Meta:
        ordering = ('-id',)
    def __str__(self):
        return str(self.usuario_username) + ": " + str(self.trailer_id)

class Historial(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    usuario_username = models.ForeignKey(User, on_delete=models.CASCADE)
    trailer_id = models.ForeignKey(Trailer, on_delete=models.CASCADE)
    fecha = models.DateField(auto_created=True,auto_now_add=True)
    class Meta:
        ordering = ('-fecha',)
    def __str__(self):
        return str(self.usuario_username) + ": " + str(self.trailer_id)