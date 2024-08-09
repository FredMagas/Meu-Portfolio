from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContatoForm
from .models import PortfolioItem, Curriculo
from django.contrib import messages
from decouple import config
import requests

# Create your views here.

def index(request):
    portfolio_items = PortfolioItem.objects.filter(publicado=True)
    curriculo = Curriculo.objects.last()  # Obtém o currículo mais recente

    if not curriculo:
        messages.error(request, 'O currículo não está disponível para download no momento.')

    if request.method == 'POST':
        form = ContatoForm(request.POST)
        
        # Capturando o token do Turnstile
        turnstile_token = request.POST.get('cf-turnstile-response')
        turnstile_secret = config('SECRET_TURNSTILE_KEY')
        
        # Verificando o token com a API do Cloudflare
        response = requests.post(
            'https://challenges.cloudflare.com/turnstile/v0/siteverify',
            data={
                'secret': turnstile_secret,
                'response': turnstile_token,
                'remoteip': request.META.get('REMOTE_ADDR')
            }
        )
        result = response.json()

        if result.get("success"):
            if form.is_valid():
                # Salvar os dados do formulário no banco de dados
                form.save()

                # Enviar e-mail
                nome = form.cleaned_data['nome']
                email = form.cleaned_data['email']
                empresa = form.cleaned_data['empresa']
                telefone = form.cleaned_data['telefone']
                media = form.cleaned_data['media']
                mensagem = form.cleaned_data['mensagem']

                subject = 'Novo contato do formulário de contato'
                content = f'''
                Nome: {nome}
                E-mail: {email}
                Empresa: {empresa}
                Telefone: {telefone}
                Onde nos encontrou: {media}
                Mensagem: {mensagem}
                '''

                email = EmailMessage(subject, content, to=['fredericomaga@hotmail.com'])
                try:
                    email.send()
                    messages.success(request, 'O formulário foi enviado com sucesso!')

                except:
                    messages.error(request, 'Ocorreu um erro ao enviar o formulário. Por favor, tente novamente mais tarde.')

                return HttpResponseRedirect(reverse('index') + '#contato')
            else:
                messages.error(request, 'Por favor, corrija os erros no formulário.')
        else:
            messages.error(request, 'Falha na verificação do Turnstile. Por favor, tente novamente.')

    else:
        form = ContatoForm()

    return render(request, 'index.html', {'portfolio_items': portfolio_items,'curriculo': curriculo, 'form': form})