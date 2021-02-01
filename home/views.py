from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,logout, login
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        return render(request, 'register.html')
def addgroup(request):
    return render(request, 'addgrp.html')
def contact(request):
    return render(request, 'contact.html')
def services(request):
    return render(request, 'service.html')
def register(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    if request.method=='POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            login(request, user)
            return redirect('/')
        else:
            print('Error')
    else:
        return render(request,'register.html')
def loginuser(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request,'login.html')
    return render(request,'login.html')
def logoutuser(request):
    logout(request)
    return redirect('/login')
def add(request):
    context = {
        'username':[],
        'amount':[],
        'descr':[],
        'amnt':'',
        'usrnm':'',
        'desc':''
    }
    sumam=0
    for i in range(1,5):
        context['amnt']='amount'+str(i)
        context['usrnm']='username'+str(i)
        context['desc']='description'+str(i)
        if request.GET[context['amnt']]=='!NULL':
            y=request.GET[context['amnt']]
            context['amount'].append(y)
            context['username'].append(request.GET[context['usrnm']])
            context['descr'].append(request.GET[context['desc']])
            print(context['amount'][i])
            #sumam = sum(context['amount'])
    sumam =len(context['amount'])


    """ am1 = int(request.GET['amount1'])
    am2 = int(request.GET['amount2'])
    am3 = int(request.GET['amount3'])
    am4 = int(request.GET['amount4']) """
    """ sumam = am1+am2+am3+am4
    nam1 = am1-sumam
    nam2 = am2-sumam
    nam3 = am3-sumam
    nam4 = am4-sumam """
    return render(request,"passbook.html",context,sumam)
def passbook(request):
    return render(request, "passbook.html")
def addindi(request):
    return render(request,"addindi.html")