from django.urls import path

from . import views

urlpatterns = [
    path('korea', views.map_korea, name="korea"),
    path('world', views.map_world, name="world"),
]