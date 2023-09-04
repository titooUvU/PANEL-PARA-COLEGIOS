from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings # usar los settings
from django.db import models
import os

def user_directory_path_profile_alumnos(instance, filename):
    # el cero es el format
    profile_picture_name = 'alumnos/{0}/profile.png'.format(instance.username)
    #que archivo guardamos..
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    #si el full_path existe lo sacamos y ponemos otro
    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_picture_name


SEXO = [
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer'),
        ('Sin informacion', 'Sin informacion'),
    ]
TIPO_USUARIO = [
        ('Profesor', 'Profesor'),
        ('Alumno', 'Alumno'),
        ('Gestor', 'Gestor'),
        ('Administrador', 'Administrador'),
    ]
TIPO_DOCUMENTO=[
        ('Sin Informacion', 'Sin Informacion'),
        ('Tarjeta de Identidad','Tarjeta de Identidad'),
        ('Cédula de Ciudadanía','Cédula de Ciudadanía'),
        ('Cédula de Extranjería', 'Cédula de Extranjería'),
        ('Registro Civil de Nacimiento','Registro Civil de Nacimiento'),
        ('Permiso Especial de Permanencia','Permiso Especial de Permanencia'),
    ]
TIPO_SANGRE = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('Desconocido', 'Desconocido'),
    ]
class CustomUserAlumno(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='alumno_grupos',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user_permissions',
        blank=True,
        related_name='alumno_permisos',
    )
    foto = models.ImageField(default='alumnos/profile.png', upload_to=user_directory_path_profile_alumnos, null=True, blank=True)
    tipo_documento = models.CharField(max_length=50,choices=TIPO_DOCUMENTO, default='Sin informacion')
    descripcion = models.TextField()
    introduccion = models.TextField()
    numero_documento = models.CharField(max_length=20, null=True, blank=True)
    tipo_usuario = models.CharField(max_length=50, choices=TIPO_USUARIO, default='Alumno')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    grado = models.ForeignKey('informacion.Grado', on_delete=models.SET_NULL, blank=True, null=True)  # Utiliza 'informacion.Grado')  # Campo ForeignKey para relacionar con Grado
    sexo = models.CharField(max_length=20, choices=SEXO, default='Sin informacion')
    estado = models.BooleanField(default=True)
    #Salud
    alergias = models.TextField(blank=True, null=True)
    condiciones_medicas = models.TextField(blank=True, null=True)
    medicamentos_actuales = models.TextField(blank=True, null=True)
    grupo_sanguineo = models.CharField(max_length=15, blank=True, null=True, choices=TIPO_SANGRE, default='Desconocido')
    contacto_emergencia_nombre = models.CharField(max_length=255, blank=True, null=True)
    contacto_emergencia_telefono = models.CharField(max_length=20, blank=True, null=True)
    #pagos
    ver_notas = models.BooleanField(default=True)
    

    def __str__(self):
        return self.username + self.tipo_usuario


def user_directory_path_profile_alumnos(instance, filename):
    # el cero es el format
    profile_picture_name = 'alumnos/{0}/profile.jpg'.format(instance.user.username)
    #que archivo guardamos..
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    #si el full_path existe lo sacamos y ponemos otro
    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_picture_name


###################################################
def user_directory_path_profile_gestor(instance, filename):
    # el cero es el format
    profile_picture_name = 'gestores/{0}/profile.png'.format(instance.username)
    #que archivo guardamos..
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    #si el full_path existe lo sacamos y ponemos otro
    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_picture_name
class CustomUserGestor(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='gestor_grupos',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='gestor_permissions',
        blank=True,
        related_name='gestor_permisos',
    )
    foto = models.ImageField(default='gestores/profile.png', upload_to=user_directory_path_profile_gestor, null=True, blank=True)
    tipo_documento = models.CharField(max_length=50,choices=TIPO_DOCUMENTO, default='Sin informacion')
    numero_documento = models.CharField(max_length=20, null=True, blank=True)
    tipo_usuario = models.CharField(max_length=50, choices=TIPO_USUARIO, default='Gestor')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    sexo = models.CharField(max_length=20, choices=SEXO, default='Sin informacion')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.username + self.tipo_usuario


def user_directory_path_profile_gestor(instance, filename):
    # el cero es el format
    profile_picture_name = 'gestores/{0}/profile.jpg'.format(instance.user.username)
    #que archivo guardamos..
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    #si el full_path existe lo sacamos y ponemos otro
    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_picture_name



#############################################################

def user_directory_path_profile_profesor(instance, filename):
    # el cero es el format
    profile_picture_name = 'profesores/{0}/profile.png'.format(instance.username)
    #que archivo guardamos..
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    #si el full_path existe lo sacamos y ponemos otro
    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_picture_name

class CustomUserProfesores(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='profesor_grupos',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='profesor_permissions',
        blank=True,
        related_name='profesor_permisos',
    )
    foto = models.ImageField(default='profesores/profile.png', upload_to=user_directory_path_profile_profesor, null=True, blank=True)
    tipo_documento = models.CharField(max_length=50,choices=TIPO_DOCUMENTO, default='Sin informacion')
    descripcion = models.TextField()
    introduccion = models.TextField()
    numero_documento = models.CharField(max_length=20, null=True, blank=True)
    tipo_usuario = models.CharField(max_length=50, choices=TIPO_USUARIO, default='Profesor')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    titular = models.ForeignKey('informacion.Grado', on_delete=models.SET_NULL, blank=True, null=True,related_name='profesor_titulares')  # Utiliza 'informacion.Grado')  # Campo ForeignKey para relacionar con Grado
    sexo = models.CharField(max_length=20, choices=SEXO, default='Sin informacion')
    estado = models.BooleanField(default=True)
    #Salud
    alergias = models.TextField(blank=True, null=True)
    condiciones_medicas = models.TextField(blank=True, null=True)
    medicamentos_actuales = models.TextField(blank=True, null=True)
    grupo_sanguineo = models.CharField(max_length=15, blank=True, null=True, choices=TIPO_SANGRE, default='Desconocido')
    contacto_emergencia_nombre = models.CharField(max_length=255, blank=True, null=True)
    contacto_emergencia_telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username + self.tipo_usuario


def user_directory_path_profile_profesor(instance, filename):
    # el cero es el format
    profile_picture_name = 'profesores/{0}/profile.jpg'.format(instance.user.username)
    #que archivo guardamos..
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    #si el full_path existe lo sacamos y ponemos otro
    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_picture_name




#######################################################################################################
def user_directory_path_profile_administrador(instance, filename):
    # el cero es el format
    profile_picture_name = 'administradores/{0}/profile.png'.format(instance.username)
    #que archivo guardamos..
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    #si el full_path existe lo sacamos y ponemos otro
    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_picture_name

class CustomUserAdministrador(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='administrador_grupos',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='administrador_permissions',
        blank=True,
        related_name='administrador_permisos',
    )
    foto = models.ImageField(default='administradores/profile.png', upload_to=user_directory_path_profile_administrador, null=True, blank=True)
    tipo_documento = models.CharField(max_length=50,choices=TIPO_DOCUMENTO, default='Sin informacion')
    cargo = models.TextField()
    introduccion = models.TextField()
    numero_documento = models.CharField(max_length=20, null=True, blank=True)
    tipo_usuario = models.CharField(max_length=50, choices=TIPO_USUARIO, default='Alumno')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    sexo = models.CharField(max_length=20, choices=SEXO, default='Sin informacion')
    estado = models.BooleanField(default=True)
    

    def __str__(self):
        return self.username + self.tipo_usuario


def user_directory_path_profile_administrador(instance, filename):
    # el cero es el format
    profile_picture_name = 'administradores/{0}/profile.jpg'.format(instance.user.username)
    #que archivo guardamos..
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    #si el full_path existe lo sacamos y ponemos otro
    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_picture_name
