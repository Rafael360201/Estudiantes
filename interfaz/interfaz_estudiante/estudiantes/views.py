import requests
from django.shortcuts import render, redirect

def lista_estudiantes(request):
    # Obtener datos de la API RESTful de Flask
    # get_usuarios
    response = requests.get('http://127.0.0.1:5000/usuarios')
    estudiantes = response.json()

    return render(request, 'estudiantes/lista_estudiantes.html', {'estudiantes': estudiantes})

def crear_estudiante(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        edad = request.POST['edad']
        correo_electronico = request.POST['correo_electronico']

        # Enviar datos al API RESTful de Flask para crear un estudiante
        data = {
            'nombre_completo': nombre,
            'edad': edad,
            'correo_electronico': correo_electronico
        }
        response = requests.post('http://localhost:5000/usuarios', json=data)

        if response.status_code == 200:
            return redirect('lista_estudiantes')

    return render(request, 'estudiantes/crear_estudiante.html')

def editar_estudiante(request, estudiante_id):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        edad = request.POST['edad']
        correo_electronico = request.POST['correo_electronico']

        # Enviar datos al API RESTful de Flask para actualizar un estudiante
        data = {
            'nombre_completo': nombre,
            'edad': edad,
            'correo_electronico': correo_electronico
        }
        response = requests.put(f'http://localhost:5000/usuarios/{estudiante_id}', json=data)

        if response.status_code == 200:
            return redirect('lista_estudiantes')

    # Obtener datos del estudiante desde el API RESTful de Flask
    response = requests.get(f'http://localhost:5000/usuarios/{estudiante_id}')
    estudiante = response.json()

    return render(request, 'estudiantes/editar_estudiante.html', {'estudiante': estudiante})

def borrar_estudiante(request, estudiante_id):
    # Enviar solicitud DELETE al API RESTful de Flask para eliminar un estudiante
    response = requests.delete(f'http://localhost:5000/usuarios/{estudiante_id}')

    if response.status_code == 200:
        return redirect('lista_estudiantes')