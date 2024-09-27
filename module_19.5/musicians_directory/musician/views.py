from django.shortcuts import render,redirect
from . import forms
from musician.models import musician_model
from musician.forms import musician_form

# Create your views here.

def musician(request):
    if(request.method == 'POST'):
        musician_form = forms.musician_form(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect("homepage")
    else:
        musician_form = forms.musician_form()
    return render(request,"musician.html",{'form' : musician_form})


def edit_musician(request,id):
    musician = musician_model.objects.get(pk = id)
    musician_form = forms.musician_form(instance=musician)
    if(request.method == "POST"):
        musician_form = forms.musician_form(request.POST,instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect("homepage")
    return render(request,"album.html",{'form' : musician_form})

