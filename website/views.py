from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
import datetime

def index(request):
    now = datetime.datetime.now()
    context = {'now': now }
    return render(request, 'website/index.html', context)
