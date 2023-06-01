from django.urls import path, include
from . import views

urlpatterns = [
    path('agendamento/', views.agendamento, name="agendamento"),
]
