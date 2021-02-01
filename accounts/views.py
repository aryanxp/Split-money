from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.
def register(request):
    if request.method=='POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            return redirect('home/')
        else:
            print('Error')
    else:
        return render(request,'register.html')