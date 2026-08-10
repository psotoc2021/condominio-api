import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient

from .models import Documento


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def usuario(db):
    return User.objects.create_user(
        username="usuario_test",
        password="clave12345",
        email="test@condominio.cl",
    )


@pytest.mark.django_db
def test_health(client):
    response = client.get(reverse("health"))
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


@pytest.mark.django_db
def test_version(client):
    response = client.get(reverse("version"))
    assert response.status_code == 200
    assert response.json()["version"] == "1.0.0"


@pytest.mark.django_db
def test_listar_usuarios(api_client, usuario):
    response = api_client.get("/api/users/")
    assert response.status_code == 200
    assert len(response.data) == 1


@pytest.mark.django_db
def test_crear_usuario_api(api_client):
    datos = {
        "username": "nuevo_usuario",
        "first_name": "Ana",
        "last_name": "Perez",
        "email": "ana@condominio.cl",
    }

    response = api_client.post("/api/users/", datos, format="json")

    assert response.status_code == 201
    assert User.objects.filter(username="nuevo_usuario").exists()


@pytest.mark.django_db
def test_modificar_usuario_api(api_client, usuario):
    response = api_client.patch(
        f"/api/users/{usuario.id}/",
        {"last_name": "Modificado"},
        format="json",
    )

    assert response.status_code == 200

    usuario.refresh_from_db()
    assert usuario.last_name == "Modificado"


@pytest.mark.django_db
def test_eliminar_usuario_api(api_client, usuario):
    response = api_client.delete(f"/api/users/{usuario.id}/")

    assert response.status_code == 204
    assert not User.objects.filter(id=usuario.id).exists()


@pytest.mark.django_db
def test_acceso_portal_requiere_autenticacion(client):
    response = client.get("/")

    assert response.status_code == 302
    assert "/login/" in response.url