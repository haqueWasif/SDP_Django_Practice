from django import forms 
from .models import practice_model

class practice_form(forms.ModelForm):
    class Meta:
        model = practice_model
        fields = '__all__'
        
