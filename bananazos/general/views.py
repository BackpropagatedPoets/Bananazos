from django.shortcuts import render, get_object_or_404
from .models import Trailer

def trailers_list(request):
    trailers = Trailer.objects
    return render(request,
                  'index.html',
                  {'trailers': trailers})