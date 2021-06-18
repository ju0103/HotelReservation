from django.shortcuts import render, redirect

def home(request):
    welcome = "Welcome to HUFS Hotel"
    return render(request, 'index/home.html', {'welcome' : welcome})

def hotel(request):
    hotel = 'About HUFS Hotel'
    return render(request, 'index/hotel.html', {'hotel' : hotel})
