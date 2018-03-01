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
   # habilidades = forms.ModelChoiceField(queryset=db_habilidades.objects.all(), label= 'Habilidades Trabalhadas',required=True , widget=forms.CheckboxSelectMultiple)    
    habilidades =  forms.MultipleChoiceField(label = 'Quais habilidades envolvidas?', required=True, widget=forms.CheckboxSelectMultiple, choices=skills_choice,    )
    metodologia = forms.CharField(label= 'O que fazer? ', widget=forms.Textarea)
  #  player_video = forms.BooleanField(label= 'Usar visualizador de vídeo?')
   # video= forms.URLField(label= 'Qual o endereço (URL) do vídeo?')
    # anotacao_texto
    # player_audio
    # player_imagem
    # carregar_video
    # carregar_audio
    # carregar_imagem 
    class Meta:
         model = db_edp
       
         fields = ('nome', 'video')
    #     'objetivo_pedagogigo',
    #     'habilidades' ,
    #     'metodologia', 
    #     'player_video',
    #     'video',
    #     'anotacao_texto',
    #     'player_audio' ,
    #     'player_imagem',
    #     'carregar_video',
    #     'carregar_audio' ,
 #        'carregar_imagem' ,)


#class EscritaForm(forms.ModelForm):

#    paragrafo = forms.CharField(widget=forms.Textarea(  {
#        'class': 'form-control',
#        'placeholder': 'digite o paragrafo'}  ))

 #   class Meta:
  #      model = db_escrita
   #     fields = ('paragrafo','posicao_paragrafo','sala')

class form_edp_aluno(forms.ModelForm):
     class Meta:
         model = db_edp_aluno
         fields = ('resposta', )