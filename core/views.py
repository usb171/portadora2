from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import JsonResponse
from django.db.models import Q

from .models import *

class Core():
    def login(request):
        if request.method == 'GET':
            auth_logout(request)
            return render(request, 'core/login.html')
        elif request.method == "POST":
            username = request.GET.get('usuario')
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)  # Faz a autenticação do usuário
            if (user is not None) and (user.is_active):  # Se existir usuário cadastrado e ele for ativo
                auth_login(request, user)  # Faz o login do usuário
                return redirect('sala')
            else:
                contexto = {'flag': False, 'msg': 'Email e Senha não correspondem', 'password': password}
                return render(request, "core/login.html", contexto)

    def sala(request):
        if request.user.is_authenticated:
            context = {'usuario': None}
            if request.method == 'GET':
               usuario = Usuario.objects.get(user=request.user)
               context['usuario'] = usuario

               if usuario.tipoStream == "1":
                   return render(request, "sala/sala.html", context)
               elif usuario.tipoStream == '2':
                   return render(request, "sala/sala.html", context)
               else:
                   auth_logout(request)
                   return redirect('login')

            else:
                auth_logout(request)
                return redirect('login')
        else:
            return redirect('login')

class CoreAjax():
    def getDadosStream(request):
        if request.user.is_authenticated:
            try:
                usuario = Usuario.objects.get(user=request.user)
                sala = Sala.objects.filter(Q(tx=usuario) | Q(rx=usuario)).first()
                data = {
                        'nomeUsuario': usuario.nome,
                        'sala': sala.nome,
                        'tipoStream': usuario.tipoStream,
                        'socketMessageEvent': sala.socketMessageEvent,
                        'server': sala.server.nome,
                        'tx': sala.tx.nome,
                        'rx': sala.rx.nome
                }
                return JsonResponse(data)
            except:
                print('Erro ao buscar dados do servidor')
                return redirect('login')

        else:
            return redirect('login')

