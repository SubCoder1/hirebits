from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout, authenticate
from AUth.forms import Registerform
# Create your views here.

@csrf_protect
def login_view(request):
    context = {}
    logout(request)
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            user.active = True
            user.save()
            login(request, user)
            return redirect('/dashboard/')
        else:
            context = { 'error':"Username or Password is incorrect!" }
    return render(request, 'login.html', context=context)

def logout_view(request):
    user = request.user
    user.active = False
    user.save()
    logout(request)
    return redirect('/')

@csrf_protect
def register_view(request):
    context = {}
    form = Registerform(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #return redirect('/home/')
                return redirect('/dashboard/')
    else:
        if form.has_error('username'):
            context['username'] = 'already exists!'
        if form.has_error('email'):
            context['email'] = 'already exists!'
    return render(request, 'register.html', context)

def reset_view(request):
    return render(request, 'reset.html', {})

def forgot_pass_view(request):
    return render(request, 'forgot.html', {})