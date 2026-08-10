from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Documento


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]


class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento

        fields = [
            "id",
            "titulo",
            "descripcion",
            "tipo",
            "archivo",
            "fecha_publicacion",
        ]