from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    correo_electronico = models.EmailField()

    class Meta:
        db_table = 'usuario'  # Cambia 'estudiantes_estudiante' por 'usuarios'

    def __str__(self):
        return self.nombre

