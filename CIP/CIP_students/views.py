from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib import messages
from CIP_students.models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Group
from django import forms

class RegisterValidation(forms.Form):
    login = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(min_length=6)

class LoginValidation(forms.Form):
    login = forms.CharField(max_length=30)
    password = forms.CharField(min_length=6)

def logout_page(request):
    logout(request)
    return redirect('/login')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        form = RegisterValidation(request.POST)
        if not form.is_valid():
            return redirect('/register')

        if User.objects.filter(username = request.POST.get('login')).exists():
                return HttpResponse('Пользователь уже существует')
        else:
                user = User() #создаем новую запись в таблице
                #ниже заполняем поля нашего Userа
                user.username = request.POST.get('login')
                user.first_name = request.POST.get('first_name')
                user.last_name = request.POST.get('last_name')
                user.email = request.POST.get('email')
                user.set_password(request.POST.get('password'))
                user.save()#обязательно сохраняем юзера

                login(request, user)
                return redirect('/page')

def login_page(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        form = LoginValidation(request.POST)
        if not form.is_valid():
            messages.add_message(request, messages.ERROR, 'Данные неверны!')
            return redirect('/login')

        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.add_message(request, messages.ERROR, 'Данные неверны!')
            return redirect('/login')
        else:
            login(request,user)
            return redirect('/')

def mainPage(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    return render(request,"main.html")

def userPage(request):
    if request.method == 'GET':
        id = request.user.id
        user = CustomUser.objects.get(pk=id)
        return render(request,'page.html',{'user':user})
def add_proj(request):
    return render(request,'add_project_form.html')
