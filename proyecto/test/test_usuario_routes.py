import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models.usuario import Usuario
from app import create_app, db

class UsuarioRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        self.client = self.app.test_client()

        # Crea algunos usuarios de prueba
        usuario1 = Usuario(nombre_completo='John Doe', edad=25, correo_electronico='johndoe@example.com')
        usuario2 = Usuario(nombre_completo='Jane Smith', edad=30, correo_electronico='janesmith@example.com')
        db.session.add_all([usuario1, usuario2])
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_usuarios(self):
        # Hacer una solicitud GET para obtener todos los usuarios
        response = self.client.get('/usuarios')

        # Verificar el código de respuesta
        self.assertEqual(response.status_code, 200)

        # Verificar la estructura de la respuesta JSON
        datos = response.json
        self.assertIsInstance(datos, list)
        self.assertEqual(len(datos), 2)

    def test_get_usuario_por_id(self):
        # Obtener el ID del primer usuario creado en el setUp()
        usuario = Usuario.query.first()
        usuario_id = usuario.id

        # Hacer una solicitud GET para obtener un usuario por ID
        response = self.client.get(f'/usuarios/{usuario_id}')

        # Verificar el código de respuesta
        self.assertEqual(response.status_code, 200)

        # Verificar la estructura de la respuesta JSON
        datos = response.json
        self.assertIsInstance(datos, dict)
        self.assertEqual(datos['id'], usuario_id)

    def test_post_usuario(self):
        # Datos de prueba
        datos_usuario = {
            'nombre_completo': 'Nuevo Usuario',
            'edad': 35,
            'correo_electronico': 'nuevousuario@example.com'
        }

        # Hacer una solicitud POST para crear un usuario
        response = self.client.post('/usuarios', json=datos_usuario)

        # Verificar el código de respuesta
        self.assertEqual(response.status_code, 200)

        # Verificar que el usuario se haya creado correctamente en la base de datos
        nuevo_usuario = Usuario.query.filter_by(nombre_completo=datos_usuario['nombre_completo']).first()
        self.assertIsNotNone(nuevo_usuario)
        self.assertEqual(nuevo_usuario.edad, datos_usuario['edad'])
        self.assertEqual(nuevo_usuario.correo_electronico, datos_usuario['correo_electronico'])

if __name__ == '__main__':
    unittest.main()
