from django.db import models


class PerfilUsuario(models.Model):
    foto_perfil = models.ImageField(upload_to='fotos_perfil')