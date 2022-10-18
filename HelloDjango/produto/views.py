from django.shortcuts import render



def metodo(request):
    return render(request, 'produto/index.html') # Este comando irá renderizar o meu html que será chamado pelo path que está no meu app.