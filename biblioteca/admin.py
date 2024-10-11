from django.contrib import admin
from biblioteca.models import Autor, Direccion, Libro, Pais


class LibroAdmin(admin.ModelAdmin):
    search_fields = ('titulo',)
    list_filter = ('autor', 'calificacion')
    list_display = ('titulo', 'autor')


admin.site.register(Autor)
admin.site.register(Direccion)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Pais)
