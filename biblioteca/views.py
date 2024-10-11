from django.db.models import Avg
from django.shortcuts import get_object_or_404, render

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


def detalle_libro(request, id):
    libro = get_object_or_404(Libro, pk=id)
    params = {
        "libro": libro,
    }
    return render(request, "biblioteca/detalle_libro.html", params)