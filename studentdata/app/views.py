from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Student
from django.http import HttpResponse
from .forms import StudentRegistration
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='login')
def index(request):
    stu = Student.objects.all()
    return render(request, "index.html", {'students': stu})

@login_required(login_url='login')
def add(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        emailid = request.POST.get('emailid')
        contactno = request.POST.get('contactno')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        stu = Student()
        print('........................................',type(stu))
        stu.name = name
        stu.roll = roll
        stu.emailid = emailid
        stu.contactno = contactno
        stu.city = city
        stu.state = state
        stu.pincode = pincode
        stu.save()
        return redirect("index")
    return render(request, 'addandshow.html')

@login_required(login_url='login')
def update(request, id):
    stu = Student.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        emailid = request.POST.get('emailid')
        contactno = request.POST.get('contactno')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        stu.name = name
        stu.roll = roll
        stu.contactno = contactno
        stu.emailid = emailid
        stu.city = city
        stu.state = state
        stu.pincode = pincode
        stu.save()
        return redirect("/index")
    return render(request, 'updatestudent.html', {'student': stu})

@login_required(login_url='login')
def update_new(request, id):
    context = {}
    obj = Student.objects.get(id=id)
    form = StudentRegistration(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/index")
    context["form"] = form
    return render(request, 'updatestudent.html', context)

@login_required(login_url='login')
def deletedata(request, id):
    stu = Student.objects.get(pk=id)
    if request.method == 'POST':
        stu.delete()
        return redirect("/index")
    return render(request, "message.html", {'student':stu})



#signup

def registerPage(request):
    form = UserCreationForm()
    if request.method=='POST':
        username = request.POST.get('username')
        password1 =request.POST.get('password1')
        password2 = request.POST.get('password2')
        print(username, password1, password2)
        if form.is_valid():
            user= User.objects.create(username,password1,password2)
            user.save()
            print('saved')
            return redirect('/login')
            messages.info(request,'User Created! Please Login Now')
    return render(request,'register.html',{'form': form})    


#Login Form

def user_login(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(request,username = username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/index')
        else:
            messages.info(request, 'username or password incorrect!')  

    fm =AuthenticationForm()
    return render(request,'login.html', {'form': fm})

def logoutuser(request):
    logout(request)
    return redirect('login')


