from django.shortcuts import render

def miVista(request):
    return render(request, 'aplicacion/miHTML.html')
