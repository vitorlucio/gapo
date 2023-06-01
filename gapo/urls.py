from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('autenticacao.urls')),
    path('', include('plataforma.urls')),
    path('sobre', include('quem_somos.urls')),
    path('doacao', include('doacao.urls')),
    path('agendamento', include('agendamento.urls')),
    path('voluntario', include('voluntario.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)