# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from reglas.rules import *
from .models import Habitacion,Filter,RoomType
import json
from django.http import JsonResponse


def index(request):
    return render(request, 'home.html',{'location':'activeh'},content_type='text/html; charset=utf-8')

def reservas(request, json_file_path='hotel/data/habitaciones.json'):
    cargar_habitaciones_desde_json(json_file_path)
    habitaciones = Habitacion.objects.filter(disponible=True)
    Filter.objects.all().delete()
    load_filters()
    filters= Filter.objects.all()
    RoomType.objects.all().delete()
    load_room_types()
    roomTypes= RoomType.objects.all()
    return render(request, 'reservas.html', {'habitaciones': habitaciones, "filters":filters,"roomTypes":roomTypes,'location':'activeh' },content_type='text/html; charset=utf-8')


def GetHabitaciones(request, json_file_path='hotel/data/habitaciones.json'):
    with open(json_file_path, 'r',encoding='utf-8') as file:
        habitaciones_data = json.load(file)
    data = {'data': habitaciones_data}
    return JsonResponse(data)

def GetTiposHab(request, json_file_path='hotel/data/room_types.json'):
    with open(json_file_path, 'r',encoding='utf-8') as file:
        habitaciones_data = json.load(file)
    data = {'data': habitaciones_data}
    return JsonResponse(data)

def filterRules(request):
    engine = RecomendarHabitacion()
    engine.reset()
    engine.declare(Residencia(residencia=request.GET["residencia"]),
                   Edad(edad=request.GET["edad"]),
                   Cantidad(cantidad=request.GET["cantidad"]),
                   Tipo(tipo=(request.GET["tipo"] if request.GET.get("tipo")!=None else "")),
                   Servicio(servicio=request.GET["servicio"] if request.GET.get("servicio")!=None else ""))
    engine.run()
    print(engine.facts)
    hechos_recomendacion = [fact for fact in engine.facts.values() if isinstance(fact, Recomendacion)]
    data = {'data': hechos_recomendacion}
    return JsonResponse(data)

def cargar_habitaciones_desde_json(json_file_path):
    with open(json_file_path, 'r',encoding='utf-8') as file:
        habitaciones_data = json.load(file)

    for habitacion_data in habitaciones_data:
        numero_habitacion = habitacion_data.get('numero')
        if not Habitacion.objects.filter(numero=numero_habitacion).exists():
            Habitacion.objects.create(**habitacion_data)

def load_filters():
    json_data='hotel/data/filters.json'
    with open(json_data,'r',encoding='utf-8') as file:
        filters_json=json.load(file)
    print(json)
    for filterd in filters_json:
        Filter.objects.create(**filterd)
def load_room_types():
    json_data='hotel/data/room_types.json'
    with open(json_data,'r',encoding='utf-8') as file:
        filters_json=json.load(file)
    print(json)
    for filterd in filters_json:
        id_room = filterd.get('id')
        if not RoomType.objects.filter(id=id_room).exists():
            RoomType.objects.create(**filterd)