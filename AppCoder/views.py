from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.

def curso(self):
    curso=Curso(nombre="curso de django",comision=12345)
    curso.save()
    texto = f'Curso: {curso.nombre} comision: {curso.comision}'
    return HttpResponse (texto)