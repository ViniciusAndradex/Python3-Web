from django.shortcuts import render
from django.http import HttpResponse

def index(request): # Index primeiro arquivo a ser chamado no blog
    return HttpResponse('Olá Mundo!') # Return um html para o meu server.
