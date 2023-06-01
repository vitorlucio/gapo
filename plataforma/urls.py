from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('evento/<str:id>', views.evento, name="evento"),
]
