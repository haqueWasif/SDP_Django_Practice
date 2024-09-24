from django.shortcuts import render,redirect
from . import forms

# Create your views here.

def home(request):
    if(request.method == 'POST'):
        practice_form = forms.practice_model(request.POST)
        if practice_form.is_valid():
            practice_form.save()
            return redirect("homepage")
    else:
        practice_form = forms.practice_form()
    return render(request,"first_app.html",{'form' : practice_form})
