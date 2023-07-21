from django import forms

from .models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'empresa', 'telefone', 'media', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail', 'required': True}),
            'empresa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Empresa', 'required': True}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone', 'required': True}),
            'media': forms.Select(attrs={'class': 'form-control'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensagem'}),
        }