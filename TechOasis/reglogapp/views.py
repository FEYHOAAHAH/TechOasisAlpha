from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm

# Create your views here

def show_start_page(request):
    return render(request, 'reglogapp/start_page.html')




def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'reglogapp/reg_page.html', {'form':form})


def show_login_page(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('products')
    else:
        form = LoginForm()
    return render(request, 'reglogapp/login_page.html', {'form': form})

