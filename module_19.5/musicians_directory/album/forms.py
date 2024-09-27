from django import forms 
from album.models import album_model

class album_form(forms.ModelForm):
    class Meta:
        model = album_model
        fields = '__all__'
        labels = {
            'Album_Name' : "Album Name",
            'Album_Release_Date' : "Album release date",
        }
        
