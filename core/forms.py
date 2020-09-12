from django import forms
from .models import Docente, Estudiante, Carrera, Curso01

#-----------------DOCENTE----------------------#
class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['nombre', 'apellido', 'edad', 'email', 'sexo']


class DocenteFormBasico(forms.Form):
    nombre = forms.CharField(label='nombre', max_length=100)
    email = forms.EmailField(label='correo',  max_length=25)

#-------------------ESTUDIANTE------------------------#
class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'edad', 'email', 'sexo']

#-------------------CARRERA-------------------------------------#
class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ['nombre', 'titulo', 'tiempo', 'jornada']


class Curso01Form(forms.ModelForm):
    class Meta:
        model = Curso01
        fields = ['alumno', 'paralelo', 'materia', 'profesor']
