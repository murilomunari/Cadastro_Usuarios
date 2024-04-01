from django.shortcuts import render
from .models import Usuario


def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    #salvar os dados da tela para o Banco de Dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    #exibir todos os usuarios ja cadastrado
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #retornar os dados para a página de listagem
    return render(request, 'usuarios/usuarios.html', usuarios)


