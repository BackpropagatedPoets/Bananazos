from django.urls import path
from . import views
app_name = 'trailers'
urlpatterns = [
    # post views
    path('', views.trailers_list, name='trailers_list'),
    path('video/<int:pk>', views.video, name="video"),
    path('historial', views.historial, name='historial'),
    path('subir_trailer', views.subir_trailer, name="subir_trailer")
]