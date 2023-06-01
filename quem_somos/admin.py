from django.contrib import admin
from .models import ImagemQuemSomos, QuemSomos

#@admin.register(QuemSomos)
#class QuemSomosAdmin(admin.ModelAdmin):
    #list_display = ('imagens','descricao')
    #list_editable = ('descricao', 'tipo')
 

admin.site.register(QuemSomos)
admin.site.register(ImagemQuemSomos)

