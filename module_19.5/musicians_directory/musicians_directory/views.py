from django.shortcuts import render 
from album.models import album_model

def home(request):
    data = album_model.objects.all()
    return render(request,"home.html",{'data' : data})