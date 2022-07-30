import datetime
from django.template import Template, Context
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render

def saludo(request):

    nombre= "david"

    temas = ["cosa1", "tarta", "cosa3"]

    ahora = datetime.datetime.now()
    #doc_externo = open("C:/Users/rafae/OneDrive/Escritorio/proyectos django/proyecto1/proyecto1/plantillas/hola.html")

    #plantilla1 = Template(doc_externo.read())

    #doc_externo.close()
    plantilla1 = get_template("hola.html")

    #contexto = Context({"nombre_persona":nombre, "fecha":ahora, "lista":temas})  

    entrada = plantilla1.render({"nombre_persona":nombre, "fecha":ahora, "lista":temas}) 
    
    return HttpResponse(entrada)


def horaActual(request):

    hora_actual = datetime.datetime.now()

    documento = """ <html>
    <body>
    <h3>
    <b>tiempo actual %s
    </b>
    </h3>
    </body>
    </html>""" % hora_actual
   
    return HttpResponse(documento)

def edadActual(request, edad, agno):

    fechaActual = 2022

    tiempoTranscurrido = agno - 2022

    edadfutura = edad + tiempoTranscurrido

    documento2= """ <html>
    <body>
    <h3>
    <b>tiempo actual %s, tiempo que paso: %s, edad en el futuro: %s
    </b>
    </h3>
    </body>
    </html>""" % (fechaActual, tiempoTranscurrido, edadfutura)

    return HttpResponse(documento2)




    
