from django.shortcuts import render, redirect

from . forms import CreateUserForm, authenticateUserForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def homepage(request):
    return render(request, 'myapp/index.html')

def register(request):
    
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/my_login')
        
    context = {'register_form': form}
    return render(request, 'myapp/register.html', context=context)

def my_login(request):
    form = authenticateUserForm()
    if request.method == 'POST':
        form = authenticateUserForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/dashboard')
            else:
                return redirect('/my_login')
    context = {'authenticateUserForm': form}
    return render(request, 'myapp/my_login.html', context=context)

def dashboard(request):
    return render(request, 'myapp/dashboard.html')

def user_logout(request):
    auth.logout(request)
    return redirect('/my_login')