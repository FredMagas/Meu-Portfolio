from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContatoForm
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == 'POST':
            form = ContatoForm(request.POST)
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
        form = ContatoForm()
    return render(request, 'index.html')