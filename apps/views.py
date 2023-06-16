from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def Homee(request):
    return render(request,'Home.html')

def Register(request):
    if request.method=="POST":
        fnam=request.POST['fname']
        sname=request.POST['sname']
        ussname=request.POST['usname']
        email=request.POST['Emails']
        passwo=request.POST['password']
        passs2=request.POST['password2']
        age = request.POST['age']
        if passwo==passs2:
            if User.objects.filter(username=ussname).exists():
               messages.info(request,"Alrready added name")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Mail already added")
            else:
                user = User.objects.create_user(username=ussname, password=passwo, email=email, first_name=fnam,
                                                last_name=sname)
                user.age = age
                user.save()
                return redirect('login')
        else:
            messages.info("Password missmatch")






    return render(request,'register.html')
def Login(request):
    if request.method == "POST":
        usname = request.POST['username']
        pawo = request.POST['pass']
        obj=auth.authenticate(username=usname,password=pawo)
        if obj is not None:
            auth.login(request,obj)
            return redirect('/')
        else:
            messages.info(request,"Please check pass username")

    return render(request,'login.html')