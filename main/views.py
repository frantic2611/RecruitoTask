from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home.html')

def greeting(request):
    name = request.GET.get('name')
    message = request.GET.get('message')
    return render(request, 'greeting.html', {'name':name, 'message':message})