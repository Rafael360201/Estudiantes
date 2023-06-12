from app import ma
from app.models.usuario import Usuario

class UsuarioSchema(ma.Schema):
    class Meta:
        model = Usuario
        fields = ('id', 'nombre_completo', 'edad', 'correo_electronico')

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)
