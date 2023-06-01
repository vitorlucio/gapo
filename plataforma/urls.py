from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('imovel/<str:id>', views.imovel, name="imovel"),
]
