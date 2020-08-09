from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('turnstyles', views.turnstyles, name='turnstyles'),
    path('materials', views.materials, name='materials'),
]