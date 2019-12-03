from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib import messages
from CIP_students.models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Group
from django import forms

from django.core.mail import send_mail
import random
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail
from django.template.defaulttags import register


class RegisterValidation(forms.Form):
    login = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(min_length=6)

class LoginValidation(forms.Form):
    login = forms.CharField(max_length=30)
    password = forms.CharField(min_length=6)

def logout_page(request):
    logout(request)
    return redirect('/student/login')


newUserInfo = {
    'leftData':False,
    'regProccess':False
}

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        form = RegisterValidation(request.POST)
        if not form.is_valid():
            messages.add_message(request, messages.ERROR, 'Данные неверны!')
            return redirect('/student/register')

        if CustomUser.objects.filter(username = request.POST.get('login')).exists():
            messages.add_message(request, messages.ERROR, 'Пользователь уже существует!')
            return redirect('/student/register')

        elif CustomUser.objects.filter(email = request.POST.get('email')).exists():
            messages.add_message(request, messages.ERROR, 'Данный email уже занят попробуйте другой!')
            return redirect('/student/register')
        else:
            newUserInfo['username'] = request.POST.get('login')
            newUserInfo['email'] = request.POST.get('email')
            newUserInfo['first_name'] = request.POST.get('first_name')

            newUserInfo['regProccess'] = True

            user = CustomUser()
            user.username = request.POST.get('login')
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.email = request.POST.get('email')
            user.set_password(request.POST.get('password'))
        
            if 'avatar' in request.FILES:
                user.avatar = request.FILES['avatar']

            user.save()

            login(request,user)

            

            chars = '+-/abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
            code = ''
            length = random.randint(5,8)
            for i in range(length):
                code += random.choice(chars)
            
            newUserInfo['code'] = code
            newUserInfo['leftData'] = True
            return redirect('/student/verification')

def register_code_enter(request):
    global newUserInfo
    if request.method == 'GET' and newUserInfo.get('leftData') == True:
        
        name = newUserInfo.get('first_name')
        code = newUserInfo.get('code')
        email = newUserInfo.get('email')

        html_message = render_to_string('email.html',{'name':name,'code':code})
        plain_message = strip_tags(html_message)
        mail.send_mail('Верификация пользователя',plain_message,settings.EMAIL_HOST_USER,[email],html_message=html_message)
        
        return render(request,'code_register.html',{'email':newUserInfo.get('email')})
    elif newUserInfo.get('leftData') == False:
        return redirect('/student/register')

    if request.method == 'POST':
        email_code = request.POST.get('email_code')
        
        if email_code == newUserInfo.get('code'):
            messages.add_message(request,messages.ERROR,'Вы успешно зарегистрировались!')
        

            newUserInfo = {
                'leftData':False,
                'regProccess':False
            }

            return redirect('/student/')
        else:
            messages.add_message(request,messages.ERROR,'Код неверен!')
            CustomUser.objects.filter(username = newUserInfo['username']).delete()
            newUserInfo = {
                'leftData':False,
                'regProccess':False
            }
            return redirect('/student/register')

def login_page(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        form = LoginValidation(request.POST)
        if not form.is_valid():
            messages.add_message(request, messages.ERROR, 'Данные неверны!')
            return redirect('/student/login')

        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.add_message(request, messages.ERROR, 'Данные неверны!')
            return redirect('/student/login')
        else:
            login(request,user)
            return redirect('/student/')

def mainPage(request):
    if not request.user.is_authenticated:
        return redirect('/student/login')

    if newUserInfo['regProccess']:
        return redirect('/student/verification')

    return render(request,"main.html")

def userPage(request):
    if not request.user.is_authenticated:
        return redirect('/student/login')
    
    if newUserInfo['regProccess']:
        return redirect('/student/verification')

    if request.method == 'GET':
        id = request.user.id
        user = CustomUser.objects.get(pk=id)
        return render(request,'page.html',{'user':user})
def add_proj(request):
    if not request.user.is_authenticated:
        return redirect('/student/login')

    if newUserInfo['regProccess']:
        return redirect('/student/verification')

    return render(request,'add_project_form.html')
