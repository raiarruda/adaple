from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import db_edp, db_habilidades, db_edp_aluno
from embed_video.fields import EmbedVideoField

skills_choice = (( 'tradução', 'tradução'), ('escrita','escrita'), ('leitura', 'leitura'))

class BootstrapAuthenticationForm(AuthenticationForm):

    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Usuário'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Senha'}))

class form_edp(forms.ModelForm):
    nome = forms.CharField(label='Nome')
    objetivo_pedagogigo = forms.CharField(label= 'O que aprender? ', widget=forms.Textarea)
    habilidades = forms.ModelChoiceField(queryset=db_habilidades.objects.all(), label= 'Habilidades Trabalhadas',required=True , widget=forms.CheckboxSelectMultiple)    
   # habilidades =  forms.MultipleChoiceField(label = 'Quais habilidades envolvidas?', required=True, widget=forms.CheckboxSelectMultiple, choices=skills_choice,    )
    metodologia = forms.CharField(label= 'O que fazer? ', widget=forms.Textarea)

    class Meta:
         model = db_edp
       
         fields = ('nome', )


class form_edp_aluno(forms.ModelForm):
     class Meta:
         model = db_edp_aluno
         fields = ('resposta', )