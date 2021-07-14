from django.forms import ModelForm 
from .models import Sequence

class Sequence_Form(ModelForm):
    class Meta:
        model = Sequence
        fields = ['sequence']
