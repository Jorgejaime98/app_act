from django.shortcuts import render, redirect, get_object_or_404   #---render y redirect tambien ocupa login
from .models import Docente, Estudiante, Carrera, Curso01
from .forms import DocenteForm, EstudianteForm, CarreraForm, Curso01Form

#------------------- USUARIO-----------------#
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
# Template tag
# block content
# extends
# url


def home(request, plantilla='home.html'):
    if request.user.is_authenticated:    # Si estamos identificados devolvemos la portada
        return render(request, plantilla)
    return redirect('login')    # En otro caso redireccionamos al login

#----------------FUNCION DOCENTES-----------------#

def docentes(request, plantilla="docentes.html"):
    docentes = list(Docente.objects.all())
    return render(request, plantilla, {'docentes': docentes})


def cursos(request, plantilla="cursos.html"):
    return render(request, plantilla)


def materias(request, plantilla="materias.html"):
    return render(request, plantilla)


def planificacion(request, plantilla="planificacion.html"):
    return render(request, plantilla)

#-----------------------FUNCION ESTUDIANTES--------------------#

def estudiantes(request, plantilla="estudiantes.html"):
    estudiantes = list(Estudiante.objects.all())
    return render(request, plantilla, {'estudiantes': estudiantes}) #--


def cursos_estudiante(request, plantilla="cursos_estudiante.html"):
    return render(request, plantilla)


def materias_estudiante(request, plantilla="materias_estudiante.html"):
    return render(request, plantilla)


def paralelo_estudiante(request, plantilla="paralelo_estudiante.html"):
    return render(request, plantilla)

#---------------------------FUNCION CARRERA-----------------------------#
def carreras(request, plantilla="carreras.html"):
    carreras = list(Carrera.objects.all())
    return render(request, plantilla, {'carreras': carreras})


def descripcion_carrera(request, plantilla="descripcion_carrera.html"):
    return render(request, plantilla)
#-----------------------------FUNCION CURSO01-----------------#

def curso01(request, plantilla="curso01.html"):
    curso01 = list(Curso01.objects.all())
    return render(request, plantilla, {'curso01': curso01})


#-----------------------------CREAR DOCENTE CRUD-----------------------#
#CREAR DOCENTE CRUD
def creardocente(request, plantilla="creardocente.html"):
    if request.method == "POST":
        formDocente = DocenteForm(request.POST or None)
        if formDocente.is_valid():
            formDocente.save()
            return redirect("docentes")#-------------------------------------------------------------va en la url
    else:
        formDocente = DocenteForm()
    return render(request, plantilla, {'formDocente': formDocente})


## MODIFICAR DOCENTE CRUD
def modificardocente(request, pk, plantilla="modificardocente.html"):
    if request.method == "POST":
        formDocente = DocenteForm(request.POST or None)
        if formDocente.is_valid():
            formDocente.save()
        return redirect("docentes")#----------------------------------------------------------------------va en la url
    else:
        docente = get_object_or_404(Docente, pk=pk)
        formDocente = DocenteForm(request.POST or None, instance=docente)
    return render(request, plantilla, {'formDocente': formDocente})


## ELIMINAR DOCENTE CRUD
def eliminardocente(request, pk, plantilla="eliminardocente.html"):
    if request.method == "POST":
        docente = get_object_or_404(Docente, pk=pk)
        formDocente = DocenteForm(request.POST or None, instance=docente)
        if formDocente.is_valid():
            docente.delete()
        return redirect("docentes")#--------------------------------------------------------------------va en la url
    else:
        docente = get_object_or_404(Docente, pk=pk)
        formDocente = DocenteForm(request.POST or None, instance=docente)


    return render(request, plantilla, {'formDocente': formDocente})


## CONSULTAR DOCENTE CRUD
def consultardocente(request, plantilla="consultardocente.html"):
    return render(request, plantilla)


#-----------------------CRUD DE ESTUDIANTE------------------------------------#

## CREAR ESTUDIANTE CRUD
def crearestudiante(request, plantilla="crearestudiante.html"):
    if request.method == "POST":
        formEstudiante = EstudianteForm(request.POST or None)
        if formEstudiante.is_valid():
            formEstudiante.save()
            return redirect("estudiantes")#-------------------------------------------------------------va en la url
    else:
        formEstudiante = EstudianteForm()
    return render(request, plantilla, {'formEstudiante': formEstudiante})


## MODIFICAR ESTUDIANTE CRUD
def modificarestudiante(request, pk, plantilla="modificarestudiante.html"):
    if request.method == "POST":
        formEstudiante = EstudianteForm(request.POST or None)
        if formEstudiante.is_valid():
            formEstudiante.save()
        return redirect("estudiantes") #-------------------------------------------------------------va en la url
    else:
        estudiante = get_object_or_404(Estudiante, pk=pk)
        formEstudiante = EstudianteForm(request.POST or None, instance=estudiante)
    return render(request, plantilla, {'formEstudiante': formEstudiante})


## ELIMINAR ESTUDIANTE CRUD
def eliminarestudiante(request, pk, plantilla="eliminarestudiante.html"):
    if request.method == "POST":
        estudiante = get_object_or_404(Estudiante, pk=pk)
        formEstudiante = EstudianteForm(request.POST or None, instance=estudiante)
        if formEstudiante.is_valid():
            estudiante.delete()
        return redirect("estudiantes")#---------------------------------------------------------------va en la url
    else:
        estudiante = get_object_or_404(Estudiante, pk=pk)
        formEstudiante = EstudianteForm(request.POST or None, instance=estudiante)


    return render(request, plantilla, {'formEstudiante': formEstudiante})


## CONSULTAR DOCENTE CRUD
def consultarestudiante(request, plantilla="consultarestudiante.html"):
    return render(request, plantilla)

#----------------------------CRUD DE LA CARRERA--------------------------#
#CREAR CARRERA CRUD
def crear_carrera(request, plantilla="crear_carrera.html"):
    if request.method == "POST":
        formCarrera = CarreraForm(request.POST or None)
        if formCarrera.is_valid():
            formCarrera.save()
            return redirect("carreras")#--------------------------------------------------------------va en la url
    else:
        formCarrera = CarreraForm()
    return render(request, plantilla, {'formCarrera': formCarrera})


## MODIFICAR CARRERA CRUD
def modificar_carrera(request, pk, plantilla="modificar_carrera.html"):
    if request.method == "POST":
        formCarrera = CarreraForm(request.POST or None)
        if formCarrera.is_valid():
            formCarrera.save()
        return redirect("carreras")#----------------------------------------------------------------va en la url
    else:
        carrera = get_object_or_404(Carrera, pk=pk)
        formCarrera = CarreraForm(request.POST or None, instance=carrera)
    return render(request, plantilla, {'formCarrera': formCarrera})


## ELIMINAR CARRERA CRUD
def eliminar_carrera(request, pk, plantilla="eliminar_carrera.html"):
    if request.method == "POST":
        carrera = get_object_or_404(Carrera, pk=pk)
        formCarrera = CarreraForm(request.POST or None, instance=carrera)
        if formCarrera.is_valid():
            carrera.delete()
        return redirect("carreras")#-------------------------------------------------------------------va en la url
    else:
        carrera = get_object_or_404(Carrera, pk=pk)
        formCarrera = CarreraForm(request.POST or None, instance=carrera)


    return render(request, plantilla, {'formCarrera': formCarrera})


## CONSULTAR CARRERA CRUD
def consultar_carrera(request, plantilla="consultar_carrera.html"):
    return render(request, plantilla)


#-----------------------------CRUD CURSO01-------------------------#
#CREAR CURSO01 CRUD
def crear_curso01(request, plantilla="crear_curso01.html"):
    if request.method == "POST":
        formCurso01 = Curso01Form(request.POST or None)
        if formCurso01.is_valid():
            formCurso01.save()
            return redirect("curso01") #----------------------------------------------------------va en la url

    else:
        formCurso01 = Curso01Form()
    return render(request, plantilla, {'formCurso01': formCurso01})


## MODIFICAR CURSO01 CRUD
def modificar_curso01(request, pk, plantilla="modificar_curso01.html"):
    if request.method == "POST":
        formCurso01 = Curso01Form(request.POST or None)
        if formCurso01.is_valid():
            formCurso01.save()
        return redirect("curso01")#--------------------------------------------------------------va en la url
    else:
        curso01 = get_object_or_404(Curso01, pk=pk)
        formCurso01 = Curso01Form(request.POST or None, instance=curso01)
    return render(request, plantilla, {'formCurso01': formCurso01})


## ELIMINAR CURSO01 CRUD
def eliminar_curso01(request, pk, plantilla="eliminar_curso01.html"):
    if request.method == "POST":
        curso01 = get_object_or_404(Curso01, pk=pk)
        formCurso01 = Curso01Form(request.POST or None, instance=curso01)
        if formCurso01.is_valid():
            curso01.delete()
        return redirect("curso01")#-----------------------------------------------------------------va en la url
    else:
        curso01 = get_object_or_404(Curso01, pk=pk)
        formCurso01 = Curso01Form(request.POST or None, instance=curso01)
    return render(request, plantilla, {'formCurso01': formCurso01})


## CONSULTAR CARRERA CRUD
def consultar_curso01(request, plantilla="consultar_curso01.html"):
    return render(request, plantilla)

#--------------------------LOGIN---------------------------------#

# Create your views here.

def login(request, plantilla="login.html"):
    form = AuthenticationForm()   # Creamos el formulario de autenticación vacío
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)   # Añadimos los datos recibidos al formulario
        if form.is_valid():   # Si el formulario es válido...
            username = form.cleaned_data['username']   # Recuperamos las credenciales validadas
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)  # Verificamos las credenciales del usuario

            if user is not None:   # Si existe un usuario con ese nombre y contraseña
                do_login(request, user)   # Hacemos el login manualmente
                return redirect("home")  # Y le redireccionamos a la portada
    return render(request, plantilla, {'form': form})   # Si llegamos al final renderizamos el formulario


def logout(request):
    do_logout(request)   # Finalizamos la sesión
    return redirect("login")   # Redireccionamos a la portada
