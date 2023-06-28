from django.shortcuts import render

# Inclui a classe HttpResponse.
from django.http import HttpResponse

#Define uma function view chamada index.
def index(request):
    return render(request, 'index.html', {'título': 'Últimos Artigos'}) # Novo returno

#Define uma function view chamada ola.
def ola(request):
    return HttpResponse('Olá django')
