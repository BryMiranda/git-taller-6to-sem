from django.http import HttpResponse

def vista_proyecto(response):
    return HttpResponse('Hola Mundo')

def vista_calificar(response):
    return HttpResponse('Hola Mundo 2')