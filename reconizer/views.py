from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(response):
    return render(response, 'reconizer/home.html', {})

def test(response):
    return HttpResponse("<h1>Hello world</h1>")