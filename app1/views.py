from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vista1(request):
    return HttpResponse("<h1>Hola, esta es la vista de app1.</h1>")

def vista2(request):
    return HttpResponse("<h1>Hola, esta es la segunda vista de app1.</h1>")
