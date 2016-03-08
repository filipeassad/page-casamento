from django.shortcuts import render



def list_convidados(request):
    return render(request, 'convidado/list_convidados.html',{})
