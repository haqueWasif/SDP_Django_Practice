from django.shortcuts import render,redirect
from . import forms
from album.models import album_model

# Create your views here.

def album(request):
    if(request.method == 'POST'):
        album_form = forms.album_form(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect("homepage")
    else:
        album_form = forms.album_form()
    return render(request,"album.html",{'form' : album_form})


def edit_album(request,id):
    album = album_model.objects.get(pk = id)
    album_form = forms.album_form(instance=album)
    if(request.method == "POST"):
        album_form = forms.album_form(request.POST,instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect("homepage")
    return render(request,"album.html",{'form' : album_form})

def delete_album(request,id):
    album = album_model.objects.get(pk = id)
    album.delete()
    return redirect("homepage")
