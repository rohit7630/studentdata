from django.shortcuts import render , redirect
from .models import Student
from django.http import HttpResponse

def index(request):
  stu = Student.objects.all()
  return render(request, "index2.html", {'students': stu})


def add(request):
  if request.method =='POST':
    print(request.POST)
    name =request.POST.get('name')
    roll =request.POST.get('roll')
    emailid =request.POST.get('emailid')
    contactno =request.POST.get('contactno')
    city =request.POST.get('city')
    state =request.POST.get('state')
    pincode =request.POST.get('pincode')
    stu = Student()
    stu.name = name
    stu.roll = roll
    stu.emailid = emailid
    stu.contactno = contactno
    stu.city = city
    stu.state = state
    stu.pincode = pincode
    stu.save()
    return redirect("index")
  return render(request,'registration.html')


def update(request,):
  if request.method =='POST':
    name =request.POST.get('name')
    roll =request.POST.get('roll')
    emailid =request.POST.get('emailid')
    contactno =request.POST.get('contactno')
    city =request.POST.get('city')
    state =request.POST.get('state')
    pincode =request.POST.get('pincode')
    stu = Student.objects.get(pk=id)
    stu.name = name
    stu.roll = roll
    stu.emailid = emailid
    stu.contactno = contactno
    stu.city = city
    stu.state = state
    stu.pincode = pincode
    

  return render(request, "edit.html")

def delete(request):
 if request.method=='POST':
  pi = Student.objects.get(pk=id)
  pi.delete()
  return redirect("/") 
  



  

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 









