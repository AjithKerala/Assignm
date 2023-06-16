from django.shortcuts import render

# Create your views here.
def Homee(request):
    return render(request,'Home.html')

def Register(request):
    return render(request,'register.html')