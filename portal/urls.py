from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register("users", views.UserViewSet, basename="users")
router.register("documents", views.DocumentoViewSet, basename="documents")


urlpatterns = [
    path("", views.inicio, name="inicio"),

    path("usuarios/", views.usuarios, name="usuarios"),
    path("usuarios/nuevo/", views.usuario_crear, name="usuario_crear"),
    path("usuarios/<int:pk>/editar/", views.usuario_editar, name="usuario_editar"),
    path("usuarios/<int:pk>/eliminar/", views.usuario_eliminar, name="usuario_eliminar"),

    path("documentos/", views.documentos, name="documentos"),
    path("documentos/nuevo/", views.documento_crear, name="documento_crear"),

    path("api/", include(router.urls)),
    path("api/health/", views.health, name="health"),
    path("api/version/", views.version, name="version"),
]