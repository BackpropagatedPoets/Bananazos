from django.shortcuts import render, get_object_or_404
from .models import Trailer

def trailers_list(request):
    return render(request,
                  'general/index.html')