from django.db.models import Avg
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, View

from biblioteca.models import Libro


def index(request):
    libros = Libro.objects.all()
    libros_activos = libros.filter(activo=True)
    libros_activos_ordenados = libros_activos.order_by("titulo")
    total_libros = libros_activos_ordenados.count()
    promedio_calificacion = libros_activos_ordenados.aggregate(Avg("calificacion"))
    params = {
        "libros": libros_activos_ordenados,
        "total_libros": total_libros,
        "promedio_calificacion": promedio_calificacion,
    }
    return render(request, "biblioteca/index.html", params)


class LibroDetailView(DetailView):
    model = Libro

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Objetos dentro de la petición.
        libro_actual = self.object
        request = self.request

        # Obtener datos de la sesión.
        id_libro_favorito = request.session.get("id_libro_favorito")

        # Variable de contexto para identificar si el libro consultado es el favorito.
        context["es_favorito"] = id_libro_favorito == str(libro_actual.pk)

        return context


class FavoritoView(View):
    def post(self, request):
        # Obtener datos de la forma.
        id_libro = request.POST["id_libro"]
        
        # Registrar los datos en la sesión.
        request.session["id_libro_favorito"] = id_libro
        
        url = reverse("biblioteca:detalle_libro", kwargs={"pk": id_libro})
        return HttpResponseRedirect(url)
