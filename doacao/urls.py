from django.urls import path, include
from . import views

urlpatterns = [
    path('doacao/', views.doacao, name="doacao"),
]
