from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse("Hola Django Equipo Coder")

def segunda_vista(request):
    return HttpResponse("<br><br> <h1>Hola mundo!</h1> ")


def miNombreEs(self, nombre):

    data = f"Mi nombre es <h1>{nombre}</h1>"
    return HttpResponse(data)

def probandoTemplate(self):
    nombre = "Santiago"
    apellido = "Torres"

    namelist = ["Gabriel", "Jimena", "Ignacio", "Patricia", "Natalia"]

    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
        "namelist": namelist
    }

    #miHtml = open("C:/Users/santi/Desktop/PythonProyecto1/Proyecto1/Proyecto1/plantillas/template1.html")
    #loader.get_template("template1.html")
    plantilla = loader.get_template("template1.html")
    #miHtml.close()
    #miContext = Context(diccionario)
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
   