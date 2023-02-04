from django import forms
from . models import Contacto, Grupo

class ContactoForm(forms.ModelForm):
   class Meta:
      model = Contacto
      exclude = ('fecha',)
      grupo =  forms.ModelChoiceField(queryset=Grupo.objects.all()) 