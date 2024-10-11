from django.db import models


class Review(models.Model):
    username = models.CharField(
        verbose_name='Nombre de Usuario',
        max_length=100
    )
    review = models.TextField(
        verbose_name='Reseña',
        max_length=255
    )
    rating = models.IntegerField(
        verbose_name='Calificación'
    )

    def __str__(self):
        return f"{self.username}: {self.rating}"