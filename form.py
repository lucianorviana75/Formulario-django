from django.forms import ModelForm 
from.models import Transação

class TransaçaoForm(ModelForm):
    class Meta:
        model = Transação
        fields =['data','descrição','valor','categoria','observação']
