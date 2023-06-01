from django.urls import path, include
from . import views

urlpatterns = [
    path('sobre/', views.quem_somos, name="quem_somos"),
]
