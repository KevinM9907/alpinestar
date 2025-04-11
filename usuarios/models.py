from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class Rol(models.Model):
    nombre = models.CharField(max_length=45, unique=True)
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

class Permiso(models.Model):
    nombre = models.CharField(max_length=45, unique=True)
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

class RolHasPermiso(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    permiso = models.ForeignKey(Permiso, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('rol', 'permiso')

class UsuarioManager(BaseUserManager):
    def create_user(self, correo, password=None, **extra_fields):
        if not correo:
            raise ValueError('El correo electrónico es obligatorio')
        if not password:
            raise ValueError('La contraseña es obligatoria')
            
        usuario = self.model(
            correo=self.normalize_email(correo),
            **extra_fields
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario
    
    def create_superuser(self, correo, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True.')
            
        return self.create_user(correo, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    celular = models.CharField(max_length=10)
    correo = models.EmailField(max_length=45, unique=True)
    estado = models.BooleanField(default=True)
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT)
    
    # Campos requeridos para el admin
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['celular', 'rol']
    
    objects = UsuarioManager()
    
    def __str__(self):
        return self.correo
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'