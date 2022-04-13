from django.shortcuts import redirect, render
from .models import Todo
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def home(request):
     user = request.user
     if request.method=="POST":
          work = request.POST['work']
          start = request.POST['start']
          finish = request.POST['finish']
          Todo.objects.create(user=request.user,work=work,start=start,finish=finish)
          user = request.user
          todos = Todo.objects.filter(user = user).all()
          return render(request,'home.html',{'todos':todos})
   
     todos = Todo.objects.filter(user = user).all()
     return render(request,'home.html',{'todos':todos})
def royxatdanotish(request):
     if request.user.is_authenticated:
             return redirect('/')
     if request.method=="POST":
          username = request.POST['username']
          psw1 = request.POST['psw1']
          psw2 = request.POST['psw2']
          if User.objects.filter(username=username).exists():
                messages.warning(request,"Bu username allaqachon ro'yxatdan o'tgan!!!")
                return redirect('/register')
          if psw1 != psw2:
                    messages.warning(request,"Bu username allaqachon ro'yxatdan o'tgan!!!")
                    return redirect('/register')
          else:
               User.objects.create_user(
                    username=username,password=psw1
               )
               messages.success(request,"Siz ro'yxatdan o'tdingiz")
               return redirect('/')
               
          
     return render(request,'register.html')
# Login

def loginPage(request):
     if request.user.is_authenticated:
        return redirect('/')
     else:
        if request.method == 'POST':
            username = request.POST['username']
            password =request.POST['psw1']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('/')
            else:
              form=f"Username or password is not correct !!!{username} {password}"
              messages.error(request,form)
              return redirect('/login')
              


        return render(request, 'login.html')

def logoutUser(request):
     logout(request)
     return redirect('/login')