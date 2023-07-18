from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def login(request):
    return render(request, 'login.html', {})

def docprofile(request):
    return render(request, 'docprofile.html', {})

def userprofile(request):
    return render(request, 'userprofile.html', {})