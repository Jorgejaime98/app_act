from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, PermissionsMixin, AbstractUser

#-----------------------TABLA MAESTRA DOCENTE, ESTUDIANTE, CARRERA-------------------#

class Docente(models.Model):
     nombre = models.CharField(max_length=200)
     apellido = models.CharField(max_length=200)
     edad = models.IntegerField(default=10)
     email = models.EmailField(default =  "ii@itsgg.edu.ec")
     sexo = models.CharField(max_length=1)
     estado = models.IntegerField(default=1)  # 1 es activo y 2 es eliminado
     user = models.CharField(max_length=15)
     user_mod = models.CharField(max_length=15)
     created = models.DateTimeField(auto_now_add=True)
     updated = models.DateTimeField(auto_now=True)

     class Meta:
         db_table="tr_docente"
         verbose_name = "docente"
         verbose_name_plural = "docentes"

     def __str__(self):
         return self.apellido + ' ' + self.nombre


class Estudiante(models.Model):
     nombre = models.CharField(max_length=200)
     apellido = models.CharField(max_length=200)
     edad = models.IntegerField(default=10)
     email = models.EmailField(default="ii@itsgg.edu.ec")
     sexo = models.CharField(max_length=1)
     estado = models.IntegerField(default=1) # 1 es activo y 2 es eliminado
     user = models.CharField(max_length=20)
     user_mod = models.CharField(max_length=20)
     created = models.DateTimeField(auto_now_add=True)
     updated = models.DateTimeField(auto_now=True)

     class Meta:
        db_table="tr_estudiante"
        verbose_name = "estudiante"
        verbose_name_plural = "estudiantes"

     def __str__(self):
         return self.apellido + ' ' + self.nombre



class Curso01(models.Model): #--
    alumno = models.CharField(max_length=200)
    paralelo = models.CharField(max_length=200)
    materia = models.CharField(max_length=200)
    profesor = models.CharField(max_length=200)
    estado = models.IntegerField(default=1)  # 1 es activo y 2 es eliminado
    user = models.CharField(max_length=20)
    user_mod = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_curso01"
        verbose_name = "curso01"
        verbose_name_plural = "cursos01"

    def __str__(self):
        return self.alumno + ' ' + self.paralelo



# , null=True

#----------------------------------TABLA MAESTRA CARRERA, PAIS, PROVINCIA,CUIDAD-----------------------#

class Carrera(models.Model):
    nombre = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    tiempo = models.CharField(max_length=200)
    jornada = models.CharField(max_length=200)
    estado = models.IntegerField(default=1)  # 1 es activo y 2 es eliminado
    user = models.CharField(max_length=20)
    user_mod = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_carrera"
        verbose_name = "carrera"
        verbose_name_plural = "carreras"

    def __str__(self):
        return self.nombre + ' ' + self.titulo


class Pais(models.Model):
    nombre = models.CharField(max_length=200)
    codigo_area = models.CharField(max_length=200)
    estado = models.IntegerField(default=1)  # 1 es activo y 2 es eliminado
    user = models.CharField(max_length=20)
    user_mod = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_pais"
        verbose_name = "pais"
        verbose_name_plural = "paises"

    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    nombre = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    codigo_prov = models.CharField(max_length=200)
    estado = models.IntegerField(default=1)  # 1 es activo y 2 es eliminado
    user = models.CharField(max_length=20)
    user_mod = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_provincia"
        verbose_name = "provincia"
        verbose_name_plural = "provincias"

    def __str__(self):
        return self.nombre + ' ' + self.region

class Ciudad(models.Model):
    nombre = models.CharField(max_length=200)
    parroquia = models.CharField(max_length=200)
    estado = models.IntegerField(default=1)  # 1 es activo y 2 es eliminado
    user = models.CharField(max_length=20)
    user_mod = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_ciudad"
        verbose_name = "ciudad"
        verbose_name_plural = "ciudad"

    def __str__(self):
        return self.nombre + ' ' + self.parroquia

#----------------------------------TABLA RELACIONAL---------------------#

#class Curso01Docente(models.Model):
#    curso01 = models.ForeignKey(Curso01, on_delete=models.CASCADE)
#    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)

#    class Meta:
#        db_table = "tr_curso01_docente"



#class CarreraPaisProvinciaCiudad(models.Model):
#    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
#    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
#    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
#    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

#    class Meta:
#        db_table = "tr_carrera_pais_provincia_ciudad"

#----------------------------------ONE TO MANY----------------------------------#

#class Materia(models.Model):
 #   nombre= models.CharField(max_length=50)
  #  cursos = models.ManyToManyField(Estudiante)
