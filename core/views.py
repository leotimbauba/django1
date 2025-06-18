from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Produto, Cliente
from .forms import ClienteForm

def index(request):
    produtos = Produto.objects.all()
    cliente = Cliente.objects.all()
    context = {
        'produtos': produtos,
        'clientes': cliente,
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def sobre(request):
    return render(request, 'sobre.html')


def produto(request, pk):
    prod = Produto.objects.get(pk=pk)
    context = {
        'produto': prod,
    }
    return render(request, 'produto.html', context)


def cliente(request, pk):
    cli = Cliente.objects.get(pk=pk)
    context = {
        'cliente': cli,
    }
    return render(request, 'cliente.html', context)

def cadastro(request, pk):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadasto')
    else:
        form = ClienteForm()

    clientes = Cliente.objects.all()
    return render(request, 'cadastro.html', {'form': form, 'clientes': clientes})
