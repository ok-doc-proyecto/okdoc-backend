from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'testFunction.html',context={'text':'hello world xx'})