from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is None:
            context = {'error':"invalid username or password"}
            return render(request, 'account/login.html', context)
        login(request,user)
        return redirect('home')
    return render(request, 'account/login.html',{})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('logout')
    return render(request, 'account/logout.html',{})