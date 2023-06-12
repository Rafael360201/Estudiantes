from flask import Blueprint, jsonify, request
from app import db
from app.models.usuario import Usuario
from app.schemas.usuario_schema import usuario_schema, usuarios_schema

usuario_bp = Blueprint('usuario_bp', __name__, url_prefix='/usuarios')

@usuario_bp.route('', methods=['GET'])
def get_usuarios():
    try:
        usuarios = Usuario.query.all()
        return jsonify(usuarios_schema.dump(usuarios))
    except KeyError:
        mensaje_error = 'Datos de usuario incompletos'
        return jsonify({'error': mensaje_error}), 400
    except Exception as e:
        mensaje_error = 'Error al listar todos los usuarios'
        return jsonify({'error': mensaje_error, 'detalle': str(e)}), 500

@usuario_bp.route('/<int:id>', methods=['GET'])
def get_usuario(id):
    try:
        usuario = Usuario.query.get(id)
        return jsonify(usuario_schema.dump(usuario))
    except KeyError:
        mensaje_error = 'Datos de usuario incompletos'
        return jsonify({'error': mensaje_error}), 400
    except Exception as e:
        mensaje_error = 'Error al obtener el usuario'
        return jsonify({'error': mensaje_error, 'detalle': str(e)}), 500
    
@usuario_bp.route('', methods=['POST'])
def add_usuario():
    try:
        nombre_completo = request.json['nombre_completo']
        edad = request.json['edad']
        correo_electronico = request.json['correo_electronico']
        nuevo_usuario = Usuario(nombre_completo, edad, correo_electronico)
        db.session.add(nuevo_usuario)
        db.session.commit()

        return jsonify(usuario_schema.dump(nuevo_usuario))
    except KeyError:
            mensaje_error = 'Datos de usuario incompletos'
            return jsonify({'error': mensaje_error}), 400
    except Exception as e:
        mensaje_error = 'Error al agregar el usuario'
        return jsonify({'error': mensaje_error, 'detalle': str(e)}), 500

@usuario_bp.route('/<int:id>', methods=['PUT'])
def update_usuario(id):
    try:
        usuario = Usuario.query.get(id)
        usuario.nombre_completo = request.json['nombre_completo']
        usuario.edad = request.json['edad']
        usuario.correo_electronico = request.json['correo_electronico']
        db.session.commit()
        return jsonify(usuario_schema.dump(usuario))

    except KeyError:
        mensaje_error = 'Datos de usuario incompletos'
        return jsonify({'error': mensaje_error}), 400
    except Exception as e:
        mensaje_error = 'Error al actualizar el usuario'
        return jsonify({'error': mensaje_error, 'detalle': str(e)}), 500


@usuario_bp.route('/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    try:
        usuario = Usuario.query.get(id)
        db.session.delete(usuario)
        db.session.commit()
        return jsonify(usuario_schema.dump(usuario))

    except KeyError:
        mensaje_error = 'Datos de usuario incompletos'
        return jsonify({'error': mensaje_error}), 400
    except Exception as e:
        mensaje_error = 'Error al borrar el usuario'
        return jsonify({'error': mensaje_error, 'detalle': str(e)}), 500
