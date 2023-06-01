from django.contrib import admin
from .models import Imagem, Cidade, DiasVisita, Horario, Imovei, Visitas, Eventos

@admin.register(Imovei)
class ImoveiAdmin(admin.ModelAdmin):
    list_display = ('rua', 'valor', 'quartos', 'tamanho', 'cidade', 'tipo')
    list_editable = ('valor', 'tipo')
    list_filter = ('cidade', 'tipo')

@admin.register(Eventos)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data', 'descricao', 'endereco')
    list_editable = ('data', 'descricao', 'endereco')

admin.site.register(Imagem)
admin.site.register(Cidade)
admin.site.register(DiasVisita)
admin.site.register(Horario)
#admin.site.register(Imovei)
admin.site.register(Visitas)