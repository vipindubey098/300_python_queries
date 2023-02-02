from django.shortcuts import render

from std_info.models import StdInfo
from . forms import StdForm

# Create your views here.
def index(request):
    if request.method == "POST":
        form = StdForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StdForm()
    students = StdInfo.objects.all() # it means that you are getting all the objects from this table and stored in the students and then send
    
    form = StdForm()
    context = {
        'form':form,
        'students':students
    }
    return render(request,"std_info/index.html", context)