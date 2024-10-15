from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    cp = models.CharField(max_length=5)

    class Meta:
        verbose_name_plural = 'Direcciones'

    def __str__(self):
        return f"{self.calle}"


class Autor(models.Model):
    direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE, null=True, related_name='autor')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, null=True)
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = 'Autores'

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    
    def __str__(self):
        return self.nombre_completo()


class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=3)

    class Meta:
        verbose_name_plural = 'Países'
    
    def __str__(self):
        return f"{self.nombre} ({self.codigo})"


class Libro(models.Model):
    disponible_en = models.ManyToManyField(Pais)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=True, related_name='libros')
    titulo = models.CharField(max_length=100)
    calificacion = models.FloatField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )
    bestseller = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("biblioteca:detalle_libro", kwargs={"pk": self.id})
    
    def __str__(self):
        return f"{self.titulo}"