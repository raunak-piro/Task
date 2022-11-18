from django.shortcuts import render,redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
from django.conf import settings
from mainApp.models import Buyer
from .models import Employee
from .models import Client
from .models import Project
def add(request):
    if (request.method == "POST"):
        e = Employee()
        e.name=request.POST.get("name")
        e.email=request.POST.get("email")
        e.phone = request.POST.get("phone")
        e.salary = request.POST.get("salary")
        e.city = request.POST.get("city")
        e.state = request.POST.get("state")
        e.save()
        
    return render(request,"add.html")

def CreateClient(request):
    if (request.method == "POST"):
        e = Client()
        e.full_name=request.POST.get("full_name")
        e.company=request.POST.get("company")
        e.phone = request.POST.get("phone")
        e.email = request.POST.get("email")
        
        e.save()
    return render(request,"CreateClient.html")

def home(request):
	return render(request,"dashboard.html")
# Create your views here.
def projects(request):
    total = Project.objects.all()
    pending = Project.objects.filter(Q(work_status__icontains='Pending'))
    Complete = Project.objects.filter(Q(work_status__icontains='Complete'))
    Ongoing = Project.objects.filter(Q(work_status__icontains='Ongoing'))

    x =len(total)
    pend = len(pending)
    Complete = len(Complete)
    Ongoing = len(Ongoing)
    return render(request,"projects.html",{'key':x,'pend':pend,'Complete':Complete,'Ongoing':Ongoing})
def CreateProject(request):
    if (request.method == "POST"):
        p = Project()
        p.project_id =  request.POST.get("project_id")
        p.project_title  = request.POST.get("project_title")
        p.department = request.POST.get("department")
        p.priority = request.POST.get("priority")
        p.client = request.POST.get("client")
        p.From_Date = request.POST.get("From_Date")
        p.To_Date = request.POST.get("To_Date")
        p.work_status = request.POST.get("work_status")
        p.save()
    return render(request,"CreateProject.html")

"""
def CreateClient(Request):
    if Request.method == "POST":
        name = Request.POST["name"]
        company = Request.POST["company"]
        phone = Request.POST["phone"]
        email = Request.POST["email"]
        new_client = client(name=name,company=company,phone=phone,email=email) 
        new_client.save()
        return redirect("/")
    else:
        return HttpResponse("Not")
    return render(Request, "CreateClient.html")
"""

def client(request):
    varab = Client.objects.all()
    x = len(varab)
    return render(request,"client.html",{'total':x})
def loginPage(Request):
    if (Request.method == "POST"):
        username = Request.POST.get("username")
        password = Request.POST.get("password")
        user = authenticate(username=username, password=password)
        if (user is not None):
            login(Request, user)
            if (user.is_superuser):
                return redirect("/admin")
            else:
                return redirect("/home")
        else:
        	return HttpResponse("Incorrect User or Password!!!!!!")
        return HttpResponse("Errors")
    return render(Request, "login.html")


def signupPage(Request):
    if (Request.method == "POST"):
        p = Request.POST.get("password")
        cp = Request.POST.get("cpassword")
        if (p == cp):
            b = Buyer()
            b.name = Request.POST.get("name")
            b.username = Request.POST.get("username")
            b.phone = Request.POST.get("phone")
            b.email = Request.POST.get("email")
            user = User(username=b.username, email=b.email)
            if (user):
                user.set_password(p)
                user.save()
                b.save()
                return redirect("/")
            else:
                messages.error(Request, "Username Already Taken!!!!!!")
        else:
            messages.error(
                Request, "Password And Confirm Password Doesn't Matched!!!")
    return render(Request, "signup.html")
def ProjectDetail(request):
    var = Project.objects.all()

    return render(request,"ProjectDetail.html",{'key':var})
def ManagerClient(request):
    varab = Client.objects.all()
    x = len(varab)
    return render(request,"ManagerClient.html",{'keyM':varab,'tot':x})