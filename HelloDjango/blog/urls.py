from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # Este path está indicando os caminhos do meu site portanto, se não houver nada o path do pai que será executado; O segundo argumento indica o que será executado quando chamado o path.
]