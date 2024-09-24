from django import forms 
from musician.models import musician_model

class musician_form(forms.ModelForm):
    class Meta:
        model = musician_model
        fields = '__all__'
        labels = {
            'First_Name' : "First Name",
            'Last_Name' : "Last Name",
            'Phone_Number' : "Phone Number",
            'Instrument_Type' : "Instrument Type",
        }
        
