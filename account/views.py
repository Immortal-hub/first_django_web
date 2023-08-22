from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login,authenticate
from .froms import LoginForm
# Create your views here.

def account_login(request):
    if request.method == "GET":
        return render(request,"account/login.html",{"form":LoginForm})
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username = cd["username"],password=cd["password"])
            if user:
                return HttpResponse("Welcome you!")
            else:
                return HttpResponse(f"你输入的账号、密码有问题！")
        else:
            return HttpResponse("你输入的账号、密码无效！")