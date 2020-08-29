from django.urls import path
from . import views
app_name = 'registro'
urlpatterns = [
    # post views
    path('registro/', views.registro, name='registro'),
]