from django.contrib import admin
from .models import *

class ServidorStreamAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ativo']
    search_fields = ['nome']
    list_filter = ['ativo']

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipoStream']
    search_fields = ['nome']
    list_filter = ['tipoStream']

class SalaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'server', 'tx', 'rx']
    search_fields = ['nome']

admin.site.register(ServidorStream, ServidorStreamAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Sala, SalaAdmin)
