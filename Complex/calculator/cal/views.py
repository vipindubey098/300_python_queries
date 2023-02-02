from django.shortcuts import render
from . forms import CalForms

# Create your views here.

def index(request):
    if request.method=="POST":
        form = CalForms()
        context = {
            'form':form
        }
    return render(request,'cal/index.html', context)
