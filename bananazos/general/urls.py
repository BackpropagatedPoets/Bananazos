from django.urls import path
from . import views
app_name = 'trailers'
urlpatterns = [
    # post views
    path('', views.trailers_list, name='trailers_list')
]