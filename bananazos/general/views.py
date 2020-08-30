from django.shortcuts import render, redirect
from .models import Trailer, TrailerForm

def trailers_list(request):
    d = [
        1, "Trailazo", "https://lorempixel.com/800/400/nature/4",
        "4:20", 320]
    l = [d] * 3
    return render(request, 'general/index.html', {"trailers":l})

def video(request, pk=0):
    d = {
        "titulo":"titulo",
        "link":"//www.youtube.com/embed/Q8TXgCzxEnw?rel=0",
        "likes":"30",
        "dislikes":"20",
        "descripcion":"asdasd",
        "video_recomendado_titulo":"siguiente", 
        "video_recomendado_duracion":"2:00", 
        "video_recomendado_miniatura":"https://lorempixel.com/800/400/nature/4",
        "video_recomendado_vistas":"430",
        "comentarios":[("hola", "mal trailer"),("alejandro", "buen trailer")]
    }
    return render(request, 'general/video.html', d)

def historial(request):
    d = [
        1, "Trailazo", "https://lorempixel.com/800/400/nature/4",
        "4:20", "320"]
    l = [d] * 3
    return render(request, 'general/historial.html', {"trailers":l})

def subir_trailer(response):
    if response.method == "POST":
        form = TrailerForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:        
        form = TrailerForm()
    return render(response, "general/subir_trailer.html", {"form":form})