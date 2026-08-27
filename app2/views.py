from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vista3(request):
    return HttpResponse("<h1>Hola, esta es la vista de app2.</h1>")

def vista4(request):
    return HttpResponse("<h1>Hola, esta es la segunda vista de app2.</h1>")