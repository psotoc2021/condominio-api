\# Portal de Administración de Condominio



Aplicación web desarrollada con Django y Django REST Framework para la administración básica de un condominio.



\## Funcionalidades



\- Autenticación de usuarios.

\- Administración CRUD de usuarios.

\- Gestión y visualización de documentos.

\- API REST.

\- Endpoint de salud `/api/health/`.

\- Endpoint de versión `/api/version/`.

\- Pruebas automatizadas mediante pytest.



\## Tecnologías



\- Python

\- Django

\- Django REST Framework

\- pytest

\- Git y GitHub



\## Proyecto DevOps



El proyecto será utilizado para implementar un flujo DevOps que incorporará control de versiones, integración continua, contenedores y despliegue en AWS.

## Pruebas automatizadas

El proyecto utiliza pytest y pytest-django para validar automáticamente sus principales funcionalidades.

Las pruebas implementadas verifican:

- Estado operativo del servicio mediante `/api/health/`.
- Versión de la aplicación mediante `/api/version/`.
- Consulta de usuarios mediante GET.
- Creación de usuarios mediante POST.
- Modificación de usuarios mediante PATCH.
- Eliminación de usuarios mediante DELETE.
- Restricción de acceso al portal para usuarios no autenticados.

Las pruebas pueden ejecutarse mediante:

    pytest -v

La ejecución validada del proyecto obtuvo un resultado de 7 pruebas aprobadas y 0 pruebas fallidas.

## Despliegue

La aplicación será desplegada mediante un flujo de Integración y Entrega Continua.

El proceso contempla:

- Control de versiones mediante Git y GitHub.
- Integración Continua mediante GitHub Actions.
- Construcción de una imagen Docker.
- Publicación de la imagen en Amazon ECR.
- Despliegue de la aplicación en AWS.
- Verificación mediante los endpoints `/api/health/` y `/api/version/`.
- Monitoreo mediante Amazon CloudWatch.
