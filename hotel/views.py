from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    contenido_html='a'
    with open('hotel/templates/home.html', 'r') as file:
        contenido_html = file.read()
    return HttpResponse(contenido_html)