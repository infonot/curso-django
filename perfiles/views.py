from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView

from perfiles.models import PerfilUsuario
from perfiles.forms import PerfilForm


def almacenar_archivo(archivo):
    with open('temp/imagen.jpg', 'wb+') as dest:
        for bloque in archivo.chunks():
            dest.write(bloque)


class PerfilUsuarioCreateView(CreateView):
    model = PerfilUsuario
    fields = '__all__'
    template_name = 'perfiles/perfil_create.html'

    def get_success_url(self):
        return reverse('perfiles:registrar')


class PerfilUsuarioListView(ListView):
    model = PerfilUsuario
    template_name = 'perfiles/perfil_list.html'
    context_object_name = 'perfiles'