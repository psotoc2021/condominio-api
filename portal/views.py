from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import DocumentoForm, UsuarioForm
from .models import Documento


@login_required
def inicio(request):
    return render(request, "portal/inicio.html")


@login_required
def documentos(request):
    lista = Documento.objects.all()
    return render(request, "portal/documentos.html", {"documentos": lista})


@login_required
def documento_crear(request):
    if request.method == "POST":
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("documentos")
    else:
        form = DocumentoForm()

    return render(request, "portal/documento_form.html", {"form": form})


@login_required
def usuarios(request):
    lista = User.objects.all()
    return render(request, "portal/usuarios.html", {"usuarios": lista})


@login_required
def usuario_crear(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            password = form.cleaned_data.get("password")

            if password:
                usuario.set_password(password)

            usuario.save()
            return redirect("usuarios")
    else:
        form = UsuarioForm()

    return render(request, "portal/usuario_form.html", {"form": form})


@login_required
def usuario_editar(request, pk):
    usuario = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save(commit=False)
            password = form.cleaned_data.get("password")

            if password:
                usuario.set_password(password)

            usuario.save()
            return redirect("usuarios")
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, "portal/usuario_form.html", {"form": form})


@login_required
def usuario_eliminar(request, pk):
    usuario = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        usuario.delete()
        return redirect("usuarios")

    return render(
        request,
        "portal/usuario_eliminar.html",
        {"usuario": usuario},
    )

from django.http import JsonResponse
from rest_framework import viewsets

from .serializers import DocumentoSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer


def health(request):
    return JsonResponse({
        "status": "ok",
        "service": "condominio-api",
    })


def version(request):
    return JsonResponse({
        "version": "1.1.0",
        "service": "condominio-api",
    })