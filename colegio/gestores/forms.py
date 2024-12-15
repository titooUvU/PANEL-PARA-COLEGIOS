from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUserManager, CustomUserStudent, CustomUserTeachers, CustomUserManager, CustomUserGuardian, CustomUserAdmin
from informacion.models import Grade, ScheduleParts, Subjects, ScheduleCourts, ActivitiesType

#imagenes de usuarios
from django.forms import ClearableFileInput


#MENEJO DE ERRORES CON BASE DE DATOS
# COMPROBAR SI HAY TABLAS O LA BASE DE DATOS ESTA VACIA...
from django.db import connection


# es
#ALGUNAS PARTES DE ESTE FORMULARIO ENCESITAS LLAMAR A LOS ESTUDIANTES, PERO ES UN PROBLEMA, YA QUE SI NO TENEMOS BASE DE DATOS PODRIAMOS OBTENER ERRORES
#POR ESO AGREGAMOS ESTA FUNCION, NOS COMPRUEBA SI HAY O NO TABLAS EN NUESTRA BASE DE DATOS, SI NO HAY TABLAS SE SALTA LAS FUNCIONES MIENTRAS SE HACEN MIGRACIONES PARA EVITAR ERRORES
#
# en
#SOME PARTS OF THIS FORM NEED TO CALL STUDENTS, BUT IT IS A PROBLEM, SINCE IF WE DO NOT HAVE A DATABASE WE COULD GET ERRORS
#THAT IS WHY WE ADDED THIS FUNCTION, IT CHECKS IF THERE ARE TABLES OR NOT IN OUR DATABASE, IF THERE ARE NO TABLES, THE FUNCTIONS ARE SKIPTED WHILE MIGRATIONS ARE BEING MADE TO AVOID ERRORS

def obtener_tablas():
    engine = connection.settings_dict['ENGINE']
    if 'sqlite' in engine:
        # SQLite
        with connection.cursor() as cursor:
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            return [table[0] for table in cursor.fetchall()]
    elif 'postgresql' in engine:
        # PostgreSQL
        with connection.cursor() as cursor:
            cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
            return [table[0] for table in cursor.fetchall()]
    else:
        raise NotImplementedError(f"No se implementó soporte para el motor de base de datos {engine}")
tablas_en_bd = obtener_tablas()


#Translate: CustomUserAlumnoForm
class CustomUserStudentForm(UserCreationForm):
    def __init__(self, *args, grado=None, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtra Grados por el colegio del estudiante por agregar (usuario en sesion)
        if grado:
            self.fields['grado'].queryset = grado
    class Meta:
        model = CustomUserStudent
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'tipo_documento', 'grado', 'sexo','password1','password2','cords','foto', 'school', 'time_zone')

        widgets = {
            'time_zone': forms.TextInput(attrs={'id':'time_zone','class': 'hidden'}),
            
            'username': forms.TextInput(attrs={'id':'username','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Nombre del usuario','autocomplete':'off'}),

            'first_name': forms.TextInput(attrs={'id':'first_name','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Nombres del usuario','autocomplete':'off'}),

            'last_name': forms.TextInput(attrs={'id':'last_name','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Apellidos del usuario'}),

            'tipo_documento': forms.Select(attrs={'id':'tipo_documento','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5'}),

            'password': forms.TextInput(attrs={
                'id': 'password',
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5',
                'placeholder': 'Contraseña',
                'autocomplete': 'current-password',
                'value': 'mkdj*F2023',
            }),

            'password1': forms.TextInput(attrs={'id': 'password1','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Contraseña'}),

            'password2': forms.TextInput(attrs={'id': 'password2','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Contraseña'}),

            'email': forms.EmailInput(attrs={'id':'email','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Email donde se puede contactar al usuario','autocomplete':'off'}),

            'grado': forms.Select(attrs={'id':'grado','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5'}),

            'sexo': forms.Select(attrs={'id':'sexo','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5'}),
            
            'cords': forms.TextInput(attrs={'class': 'cords hidden', 'id':'cords'}),
            'foto': ClearableFileInput(attrs={ "class":"block w-full text-lg text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 p-2.5", "id":"input-file", "type":"file","accept":".png,.jpg,.jpeg","name":"input-file"}),
            
        }

#Translate: CustomUserGestorForm
class CustomUserManagerForm(UserCreationForm):
    class Meta:
        model = CustomUserManager
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'tipo_documento', 'sexo','password1','password2', 'school','cords','foto', 'time_zone')

        widgets = {
            'time_zone': forms.TextInput(attrs={'id':'time_zone','class': 'hidden'}),
            'username': forms.TextInput(attrs={'autocomplete': 'off','id':'username','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Nombre del usuario'}),

            'first_name': forms.TextInput(attrs={'autocomplete': 'off','id':'first_name','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Nombres del usuario'}),

            'last_name': forms.TextInput(attrs={'id':'last_name','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Apellidos del usuario'}),

            'tipo_documento': forms.Select(attrs={'id':'tipo_documento','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5'}),

            'password': forms.TextInput(attrs={
                'id': 'password',
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5',
                'placeholder': 'Contraseña',
                'autocomplete': 'current-password',
                'value': 'mkdj*F2023',
            }),

            'password1': forms.TextInput(attrs={'id': 'password1','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Contraseña'}),

            'password2': forms.TextInput(attrs={'id': 'password2','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Contraseña'}),

            'email': forms.EmailInput(attrs={'autocomplete': 'off','id':'email','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Email donde se puede contactar al usuario'}),

            'sexo': forms.Select(attrs={'id':'sexo','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5'}),
            
            'cords': forms.TextInput(attrs={'class': 'cords hidden', 'id':'cords'}),
            'foto': ClearableFileInput(attrs={ "class":"block w-full text-lg text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 p-2.5", "id":"input-file", "type":"file","accept":".png,.jpg,.jpeg","name":"input-file"}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


#Translate: CustomUserAdministradorForm
class CustomUserAdminForm(UserCreationForm):
    class Meta:
        model = CustomUserAdmin
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'tipo_documento','sexo','password1','password2', 'introduccion','cargo', 'school','cords','foto', 'time_zone')

        widgets = {
            'time_zone': forms.TextInput(attrs={'id':'time_zone','class': 'hidden'}),
            
            'username': forms.TextInput(attrs={'autocomplete': 'off','id':'username','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Numero De Documento'}),

            'first_name': forms.TextInput(attrs={'autocomplete': 'off','id':'first_name','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Nombres del usuario'}),

            'last_name': forms.TextInput(attrs={'id':'last_name','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Apellidos del usuario'}),

            'tipo_documento': forms.Select(attrs={'id':'tipo_documento','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5'}),

            'password': forms.TextInput(attrs={
                'id': 'password',
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5',
                'placeholder': 'Contraseña',
                'autocomplete': 'current-password',
                'value': 'mkdj*F2023',
            }),

            'password1': forms.TextInput(attrs={'id': 'password1','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Contraseña'}),

            'password2': forms.TextInput(attrs={'id': 'password2','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Contraseña'}),

            'email': forms.EmailInput(attrs={'autocomplete': 'off', 'id':'email','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Email donde se puede contactar al usuario'}),

            'sexo': forms.Select(attrs={'id':'sexo','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5'}),

            'introduccion': forms.TextInput(attrs={'id':'introduccion','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Descripcion'}),

            'cargo': forms.TextInput(attrs={'id':'cargo','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Descripcion'}),
            
            'cords': forms.TextInput(attrs={'class': 'cords hidden', 'id':'cords'}),
            'foto': ClearableFileInput(attrs={ "class":"block w-full text-lg text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 p-2.5", "id":"input-file", "type":"file","accept":".png,.jpg,.jpeg","name":"input-file"}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


#Translate: CustomUserProfesoresForm
class CustomUserTeachersForm(UserCreationForm):
    def __init__(self, *args, titular=None, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtra Grados por el school del estudiante por agregar (usuario en sesion)
        if titular:
            self.fields['titular'].queryset = titular
    class Meta:
        model = CustomUserTeachers
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'tipo_documento', 'titular', 'sexo','password1','password2', 'descripcion', 'school','cords','foto', 'time_zone')

        widgets = {
            'time_zone': forms.TextInput(attrs={'id':'time_zone','class': 'hidden'}),
            
            'username': forms.TextInput(attrs={'autocomplete': 'off','id':'username','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Numero De Documento'}),

            'first_name': forms.TextInput(attrs={'autocomplete': 'off','id':'first_name','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Nombres del usuario'}),

            'last_name': forms.TextInput(attrs={'id':'last_name','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Apellidos del usuario'}),

            'tipo_documento': forms.Select(attrs={'id':'tipo_documento','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5'}),

            'password': forms.TextInput(attrs={
                'id': 'password',
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5',
                'placeholder': 'Contraseña',
                'autocomplete': 'current-password',
                'value': 'mkdj*F2023',
            }),

            'password1': forms.TextInput(attrs={'id': 'password1','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Contraseña'}),

            'password2': forms.TextInput(attrs={'id': 'password2','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Contraseña'}),

            'email': forms.EmailInput(attrs={'autocomplete': 'off','id':'email','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Email donde se puede contactar al usuario'}),

            'titular': forms.Select(attrs={'id':'titular','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5'}),

            'sexo': forms.Select(attrs={'id':'sexo','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5'}),

            'descripcion': forms.TextInput(attrs={'id':'descripcion','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Descripcion'}),
            
            'cords': forms.TextInput(attrs={'class': 'cords hidden', 'id':'cords'}),
            'foto': ClearableFileInput(attrs={ "class":"block w-full text-lg text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 p-2.5", "id":"input-file", "type":"file","accept":".png,.jpg,.jpeg","name":"input-file"}),
        }


#Translate: CustomUserAcudienteForm
class CustomUserGuardianForm(UserCreationForm):
    def __init__(self, *args, estudiantes_school=None, **kwargs):
        super().__init__(*args, **kwargs)
        if estudiantes_school:
            self.fields['estudiante'].queryset = CustomUserStudent.objects.filter(school=estudiantes_school)
    class Meta:
        model = CustomUserGuardian
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'tipo_documento','password1','password2', 'introduccion', 'estudiante','sexo', 'school', 'time_zone')

        widgets = {
            'time_zone': forms.TextInput(attrs={'id':'time_zone','class': 'hidden'}),
            
            'estudiante': forms.CheckboxSelectMultiple(attrs={'id':'estudiante','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-orange-600 block w-20 p-2.5 estudiantes', 'placeholder': 'estudiante', 'id':'checkbox'}),

            'username': forms.TextInput(attrs={'id':'username','autocomplete': 'off','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Numero De Documento'}),

            'first_name': forms.TextInput(attrs={'id':'first_name','autocomplete': 'off','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Nombres del usuario'}),

            'last_name': forms.TextInput(attrs={'id':'last_name','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Apellidos del usuario'}),

            'tipo_documento': forms.Select(attrs={'id':'tipo_documento','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5'}),

            'password': forms.TextInput(attrs={
                'id': 'password',
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5',
                'placeholder': 'Contraseña',
                'autocomplete': 'current-password',
                'value': 'mkdj*F2023',
            }),

            'password1': forms.TextInput(attrs={'id': 'password1','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Contraseña'}),

            'password2': forms.TextInput(attrs={'id': 'password2','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Contraseña'}),

            'email': forms.EmailInput(attrs={'id':'email','autocomplete': 'off','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Email donde se puede contactar al usuario'}),

            'sexo': forms.Select(attrs={'id':'sexo','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5'}),
        }

#Tranlate: GradoForm
class GradeForm(forms.ModelForm):
    def __init__(self, *args, horario_partes=None, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtra los estudiantes por los proporcionados
        if horario_partes:
            self.fields['horario_partes'].queryset = ScheduleParts.objects.filter(colegio=horario_partes)
        else:
            self.fields['horario_partes'].queryset = ScheduleParts.objects.none()

    class Meta:
        model = Grade
        #fields = '__all__' 
        fields = ('grado_nom', 'grado_num', 'descripcion', 'horario_partes', 'colegio')
        widgets = {
             'grado_nom': forms.TextInput(attrs={'id':'grado_nom','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Nombre del grado'}),

             'grado_num': forms.TextInput(attrs={'id':'grado_num','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Numero de grado + letra'}),

             'descripcion': forms.TextInput(attrs={'id':'descripcion','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Descripcion del grado'}),

             'horario_partes': forms.Select(attrs={'id':'horario_partes','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5'}),
        }


#Translate: Horarios_PartesForm
class SchedulePartsForm(forms.ModelForm):
    class Meta:
        model = ScheduleParts
        fields = ('titulo', 'descripcion', 'horas', 'cortes')
        opciones_horas = [(i, f'{i} horas') for i in range(3, 23)]
        opciones_corte = [(i, f'{i} cortes') for i in range(1, 7)]
        widgets = {
            'titulo': forms.TextInput(attrs={'id':'titulo','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Nombre del Horario'}),
            'descripcion': forms.TextInput(attrs={'id':'descripcion','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Este horario...'}),
            'horas': forms.Select(attrs={'id':'horas','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5'}, choices=opciones_horas),
            'cortes': forms.Select(attrs={'id':'cortes','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5'}, choices=opciones_corte),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


#Tranlate: MateriasForm
class SubjectsForm(forms.ModelForm):
    def __init__(self, *args, estudiantes_grado=None, profesores=None, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtra los estudiantes por los proporcionados
        if estudiantes_grado:
            self.fields['profe1'].queryset = profesores
            self.fields['profe2'].queryset = profesores
            self.fields['alumnos1'].queryset = estudiantes_grado
            self.fields['alumnos2'].queryset = estudiantes_grado
    class Meta:
        model = Subjects
        fields = ['profe1', 'picture1', 'cords', 'locate1', 'locate2', 'profe2', 'electiva', 'titulo1', 'descripcion1', 'alumnos1', 'titulo2', 'descripcion2', 'alumnos2']
        widgets = {
            'profe1': forms.Select(attrs={'id':'profe1','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5'}),
            
            'picture1': ClearableFileInput(attrs={ "class":"block w-full text-lg text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 p-2.5", "id":"input-file", "type":"file","accept":".png,.jpg,.jpeg","name":"input-file"}),

            'profe2': forms.Select(attrs={'id':'profe2','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5'}),

            'electiva': forms.CheckboxInput(attrs={'class': 'w-12 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 focus:ring-2', 'id':'Checkbox'}),

            'titulo1': forms.TextInput(attrs={'id':'titulo1','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Titulo1'}),

            'descripcion1': forms.TextInput(attrs={'id':'descripcion1','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Descripcion1'}),
            
            'locate1': forms.TextInput(attrs={'id':'locate1','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Ubicacion'}),


            'alumnos1': forms.CheckboxSelectMultiple(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-orange-600 block w-20 p-2.5 ', 'placeholder': 'alumnos1', 'id':'checkbox_es_1'}),

            'titulo2': forms.TextInput(attrs={'id':'titulo2','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Titulo2'}),

            'descripcion2': forms.TextInput(attrs={'id':'descripcion2','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Descripcion2'}),
            
            'locate2': forms.TextInput(attrs={'id':'locate2','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Ubicacion'}),

            'alumnos2': forms.CheckboxSelectMultiple(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-orange-600 block w-20 p-2.5 ', 'placeholder': 'alumnos2', 'id':'checkbox_es_2'}),
            
            'cords': forms.TextInput(attrs={'class': 'cords hidden', 'id':'cords'}),
            }


#Tranlate: HrarioCortesForm
class ScheduleCourtsForm(forms.ModelForm):
    class Meta:
        model = ScheduleCourts
        fields = ['fecha_inicio', 'fecha_fin']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'id':'fecha_inicio','class': 'mt-1 p-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:border-orange-300', 'type':'date'}),
            'fecha_fin': forms.DateInput(attrs={'id':'fecha_inicio','class': 'mt-1 p-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:border-orange-300', 'type':'date'}),
        }

#Tranlate: ActividadesTipoForm     
class ActivitiesTypeForm(forms.ModelForm):
    class Meta:
        model = ActivitiesType
        fields = ('titulo', 'descripcion')
        widgets = {
            'titulo': forms.TextInput(attrs={'id':'titulo','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Nombre del Horario'}),
            'descripcion': forms.TextInput(attrs={'id':'descripcion','class': 'bg-gray-50 border border-gray-300 text-gray-900 text-lg rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5', 'placeholder': 'Este horario...'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)