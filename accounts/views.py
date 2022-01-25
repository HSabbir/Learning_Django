from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('login')

    context = {"form":form}
    return render(request, 'account/register.html',context)


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_obj = form.get_user()
            login(request,user_obj)
            return redirect('home')
    else:
        form = AuthenticationForm(request)

    context = {"form":form}
    return render(request, 'account/login.html',context)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('logout')
    return render(request, 'account/logout.html',{})