from django.db import models


class Documento(models.Model):
    TIPO_CHOICES = [
        ("ACTA", "Acta"),
        ("CUENTA", "Estado de cuenta"),
        ("COMUNICADO", "Comunicado"),
        ("OTRO", "Otro"),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default="OTRO")
    archivo = models.FileField(upload_to="documentos/")
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-fecha_publicacion"]

    def __str__(self):
        return self.titulo