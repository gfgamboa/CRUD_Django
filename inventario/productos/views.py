from django.shortcuts import render, HttpResponse


def holaMundo(request):
    return HttpResponse("Hola Mundo ADSO")

def inicio(request):
    return render(request, 'inicio.html')

# Create your views here.
