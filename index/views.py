from django.shortcuts import render

from .models import welcome

# Create your views here.


def home(request):
    welldata = welcome.objects.all()[0]
    context = {
        'welcome': welldata,
    }
    return render(request, "index.html",context)
