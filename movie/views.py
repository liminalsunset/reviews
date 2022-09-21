from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    searchTerm = request.GET.get('searchMovie')
    return render(request, 'home.html', {'searchTerm': searchTerm})

def about(request):
    return HttpResponse('<h1>Welcome to the About Page</h1>')