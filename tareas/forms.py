from django.forms import DateInput, ModelForm
from . models import Tarea

class TareaForm(ModelForm):
   class Meta: 
      model = Tarea 
      exclude = ('fechainicio',) 
      widgets = {
         'fecha_fin': DateInput(attrs={'type':'date'}),
      
      }
      
        