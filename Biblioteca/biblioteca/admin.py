from django.contrib import admin
from .models import *

class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'codigo']

class LibroAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'titulo', 'editorial', 'paginas', 'autor']

class EjemplarAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'localizacion', 'libro']

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['telefono', 'codigo', 'nombre', 'direccion']
# Register your models here.

admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Ejemplar, EjemplarAdmin)
admin.site.register(Usuario, UsuarioAdmin)
