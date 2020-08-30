from django.shortcuts import render, redirect
from .models import Trailer, TrailerForm, Comentario, Historial
from random import choice

def trailers_list(request):
    trailers = Trailer.objects.all()
    """
    d = [
        1, "Trailazo", "https://lorempixel.com/800/400/nature/4",
        "4:20", 320]
    l = [d] * 3
    """
    return render(request, 'general/index.html', {"trailers":trailers})

def video(request, pk=0):
    trailer = Trailer.objects.get(id=pk)
    trailer_siguiente = choice(Trailer.objects.all())
    comentarios = Comentario.objects.all()
    nuevo = Historial(trailer_id=trailer, usuario_username=request.user)
    nuevo.save()
    d = {
        "titulo":trailer.titulo,
        "link":trailer.link_video,
        "likes":trailer.likes,
        "dislikes":trailer.dislikes,
        "descripcion":"asdasd",
        "video_recomendado_titulo":trailer_siguiente.titulo, 
        "video_recomendado_duracion":trailer_siguiente.duracion, 
        "video_recomendado_miniatura":trailer_siguiente.link_imagen,
        "video_recomendado_vistas":trailer_siguiente.vistas,
        "comentarios":comentarios
    }
    return render(request, 'general/video.html', d)

def historial(request):
    historial = Historial.objects.filter(usuario_username=request.user)
    trailers = Trailer.objects.filter(id=historial.trailer_id)
    """
    d = [
        1, "Trailazo", "https://lorempixel.com/800/400/nature/4",
        "4:20", "320"]
    l = [d] * 3
    """
    return render(request, 'general/historial.html', {"trailers":trailers})

def subir_trailer(response):
    if response.method == "POST":
        form = TrailerForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:        
        form = TrailerForm()
    return render(response, "general/subir_trailer.html", {"form":form})

def lista_usuarios(response):
    return render(response, "general/lista_usuarios.html")

def usuario(response, username):
    d = {}
    return render(response, "general/usuario.html", d)