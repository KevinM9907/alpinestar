from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, correo, password=None, **extra_fields):
        if not correo:
            raise ValueError('El correo es obligatorio')
        usuario = self.model(
            correo=self.normalize_email(correo),
            **extra_fields
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

class Usuario(AbstractBaseUser):
    celular = models.CharField(max_length=10)
    correo = models.EmailField(max_length=45, unique=True)  # ¡Único!
    estado = models.BooleanField(default=True)
    rol = models.ForeignKey('Rol', on_delete=models.CASCADE)
    
    # Campos requeridos para AbstractBaseUser
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    
    objects = UsuarioManager()
    
    USERNAME_FIELD = 'correo'  # Campo usado para login
    REQUIRED_FIELDS = ['celular']  # Campos requeridos para createsuperuser

    def __str__(self):
        return self.correo

class Rol(models.Model):
    nombre = models.CharField(max_length=45)
    estado = models.BooleanField()

class Permiso(models.Model):
    nombre = models.CharField(max_length=45)
    estado = models.BooleanField()
    
class RolHasPermiso(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    permiso = models.ForeignKey(Permiso, on_delete=models.CASCADE)