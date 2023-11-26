from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from reglas.rules import *
from .models import Habitacion
import json


def index(request):
    contenido_html='a'
    with open('hotel/templates/home.html', 'r') as file:
        contenido_html = file.read()
    return HttpResponse(contenido_html)

def reservas(request, json_file_path='hotel/data/habitaciones.json'):
    cargar_habitaciones_desde_json(json_file_path)
    habitaciones = Habitacion.objects.filter(disponible=True)
    return render(request, 'reservas.html', {'habitaciones': habitaciones, 'titulo':'HOTEL MICA' })

def filterRules(request):
    engine = ReservarHabitacion()
    engine.reset()
    engine.declare(Residencia(tipo="nativo"))
    engine.run()
    contenido_html=engine.resultados["residencia"]
    return HttpResponse(contenido_html)

def cargar_habitaciones_desde_json(json_file_path):
    with open(json_file_path, 'r') as file:
        habitaciones_data = json.load(file)

    for habitacion_data in habitaciones_data:
        numero_habitacion = habitacion_data.get('numero')
        if not Habitacion.objects.filter(numero=numero_habitacion).exists():
            Habitacion.objects.create(**habitacion_data)