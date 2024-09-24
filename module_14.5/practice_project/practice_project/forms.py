from django import forms
from django.forms.widgets import NumberInput


class practice_forms(forms.Form):
    name = forms.CharField(initial='Enter Your Name')
    comment = forms.CharField(widget=forms.Textarea)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField(required=False)
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    BIRTH_YEAR_CHOICES = ['2003','2004','2005']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    balance = forms.DecimalField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
    choice = [('S','Small'),('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices=choice,widget=forms.RadioSelect)
    meal = [('C','Chicken'),('M','Mashroom'),('B','Beef')]
    pizza = forms.MultipleChoiceField(choices=meal,widget=forms.CheckboxSelectMultiple)
