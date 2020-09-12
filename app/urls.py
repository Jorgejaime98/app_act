"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
#include

#------------------ CRUD DE DOCENTE--------------------#
urlpatterns = [
    path('', views.home, name="home"),
    path('docentes/', views.docentes, name="docentes"),
    path('creardocente/', views.creardocente, name="creardocente"),
    path('modificardocente/<int:pk>', views.modificardocente, name="modificardocente"),
    path('eliminardocente/<int:pk>', views.eliminardocente, name="eliminardocente"),


    path('cursos/', views.cursos, name="cursos"),
    path('materias/', views.materias, name="materias"),
    path('planificacion/', views.planificacion, name="planificacion"),

    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),

#--------------------CRUD DE ESTUDIANTE-----------------------#
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('crearestudiante/', views.crearestudiante, name="crearestudiante"),
    path('modificarestudiante/<int:pk>', views.modificarestudiante, name="modificarestudiante"),
    path('eliminarestudiante/<int:pk>', views.eliminarestudiante, name="eliminarestudiante"),

    path('cursos_estudiante/', views.cursos_estudiante, name="cursos_estudiante"),
    path('materias_estudiante/', views.materias_estudiante, name="materias_estudiante"),
    path('paralelo_estudiante/', views.paralelo_estudiante, name="paralelo_estudiante"),

#----------------------CRUD DE LA CARRERA--------------------------------#
    path('carreras/', views.carreras, name="carreras"),
    path('crear_carrera/', views.crear_carrera, name="crear_carrera"),
    path('modificar_carrera/<int:pk>', views.modificar_carrera, name="modificar_carrera"),
    path('eliminar_carrera/<int:pk>', views.eliminar_carrera, name="eliminar_carrera"),

    path('descripcion_carrera/', views.descripcion_carrera, name="descripcion_carrera"),

#------------------------CRUD DE CURSO01------------------
    path('curso01/', views.curso01, name="curso01"),
    path('crear_curso01/', views.crear_curso01, name="crear_curso01"),
    path('modificar_curso01/<int:pk>', views.modificar_curso01, name="modificar_curso01"),
    path('eliminar_curso01/<int:pk>', views.eliminar_curso01, name="eliminar_curso01"),
    path('admin/', admin.site.urls),
]

# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']