from django.shortcuts import render
from .forms import practice_forms

# Create your views here.

def home(request):
    if (request.method == 'POST'):
        form = practice_forms(request.POST,request.FILES)
        return render(request,"base.html",{'form' : form})
    else:
        form = practice_forms()
    return render(request,"base.html",{'form' : form})