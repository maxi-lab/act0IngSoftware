from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hola esta es la vista index de polls.")
def detail(request, question_id):
    return HttpResponse("Viendo la pregunta %s." % question_id)


def results(request, question_id):
    response = "Resultados %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Votando %s." % question_id)