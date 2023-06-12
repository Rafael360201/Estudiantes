"""
URL configuration for interfaz_estudiante project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from estudiantes.views import lista_estudiantes
from estudiantes.views import crear_estudiante
from estudiantes.views import editar_estudiante
from estudiantes.views import borrar_estudiante


app_name = 'estudiantes'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('estudiantes/', lista_estudiantes, name='lista_estudiantes'),
    path('crear/', crear_estudiante, name='crear_estudiante'),
    path('editar/<int:estudiante_id>/', editar_estudiante, name='editar_estudiante'),
    path('borrar/<int:estudiante_id>/', borrar_estudiante, name='borrar_estudiante'),
]


