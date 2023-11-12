from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login # login함수와 이름이 겹쳐서
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request) : 
    if request.method=='POST' :
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid() :
            # 세션 CREATE/ form.get_user는 User 객체 반환
            auth_login(request, form.get_user())
            return redirect('/') # 로그인 성공시 메인페이지 이동
    else :
        form = AuthenticationForm()

    context = {
        'form' : form,
    }
    return render(request, 'user/login.html', context)


def logout(request) :
    auth_logout(request)
    return redirect('/')

def signup(request) :
    if request.method== "POST" :
        form = UserCreationForm(request.POST)
        if form.is_valid() :
            user = form.save()
            auth_login(request, user)
            return redirect('/')
    else : # 회원가입 페이지 첫 접근
        form = UserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'user/signup.html', context)


def mypage(request) :
    return render(request, 'user/mypage.html')

def delete(request) :
    data = User.objects.all()
    data.delete()
    return redirect('ranking')