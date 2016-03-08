from django.shortcuts import render
from .models import Post



def list_convidados(request):
    post = Post.objects.all()
    return render(request, 'convidado/list_convidados.html',{'posts': post})
