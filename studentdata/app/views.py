from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Student
from django.http import HttpResponse
from .forms import StudentRegistration


def index(request):
  stu = Student.objects.all()
  return render(request, "index.html", {'students': stu})


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


def update_new(request,id):
    context ={}
    obj = Student.objects.get(id=id)
    form= StudentRegistration(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect("/index")
    context["form"] = form
    return render(request,'updatestudent.html', context)    


def deletedata(request,id):
    if request.method =='POST':
        stu= Student.objects.get(pk=id)
        stu.delete()
        return redirect("index")


