from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

def list_convidados(request):
    post = Post.objects.all()
    return render(request, 'convidado/list_convidados.html', {'posts': post})
def detalhe(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'convidado/detalhe.html', {'post': post})

def novo_convidado(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('convidado.views.detalhe', pk = post.id)

    else:
        form = PostForm()
        return render(request, 'convidado/novo_convidado.html', {'form': form})

def mapa_casamento(request):
    return render(request, 'convidado/mapa_exemplo.html')

