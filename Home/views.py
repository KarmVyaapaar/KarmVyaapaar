from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User
from Home.models import Workers, Employer
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.utils.translation import gettext as _
# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        employer = Employer.objects.get(username=username)
        user = authenticate(username= username, password= password)
        if user is not None:
            login(request, user)
            return render(request,'Home/employerprofile-index.html',{'employer':employer})
        else:
            messages.info(request,'invalid credential')
            return redirect("/")
    else:
        return render(request,'Home/index.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        firstname = request.POST.get('firstname')
        lastname= request.POST.get('lastname')
        address = request.POST.get('address')
        Phone = request.POST.get('phone')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username,password=password1, email=email, first_name= firstname, last_name=lastname)
                user.save()
                employer = Employer(username=username,firstname=firstname,lastname=lastname,phone=Phone,email=email,address=address)
                employer.save()
                print(Employer.objects.all())
                print('user is created')
                return redirect("/employerprofile")
        else:
            messages.info(request,'password is not matching..')
            return redirect('/register')
    else:
        return render(request,'Home/register.html')


def employ(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request, 'Home/employerprofile-index.html')

def worker(request):
    if request.method == "POST":
        name = request.POST.get('Wname')
        email = request.POST.get('Wemail')
        password1 = request.POST.get('Wpassword1')
        password2 = request.POST.get('Wpassword2')
        Phone = request.POST.get('WPhone')
        skills = request.POST.get('skill')
        address = request.POST.get('Waddress')
        if password1 == password2:
            if User.objects.filter(username=name).exists():
                messages.info(request, 'Username Taken')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('/register')
            else:
                user = User.objects.create_user(username=name, password=password1, email=email)
                user.save()
                worker = Workers(name=name, password=password1, email=email, Phone= Phone, skills= skills,address=address,date= datetime.today())
                worker.save()
                print('user is created')
                return redirect("/worker")
        else:
            messages.info(request,'password is not matching..')
            return redirect('/register')
    else:
        if request.user.is_anonymous:
            return redirect("/")
        return render(request, 'Home/worker-index.html')

def history(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request,'Home/history.html')

def notify(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request,'Home/notification.html')

def FAQ(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request,'Home/FAQs.html')

def logoutuser(request):
    logout(request)
    return redirect("/")

def loginWorker(request):
    if request.method == "POST":
        name = request.POST.get('wusername')
        password = request.POST.get('wpassword')
        worker = Workers.objects.get(name=name)
        print(worker)
        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
            return render(request,'Home/worker-index.html',{'worker':worker})
    else:
        return render(request,'Home/index.html')

def search(request):
    if request.user.is_anonymous:
        return redirect("/")
    qur = request.GET.get('search')
    workers = Workers.objects.filter(skills = qur)
    print(workers)
    return render(request, 'Home/search.html',{'workers':workers})
