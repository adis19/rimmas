from django.shortcuts import render, redirect
from .models import *
from .form import Registration
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def main(request):
    prop_value = Products.objects.all()
    return render(request, 'main.html',{'prop_key':prop_value})

def about(request):
    return render(request,'about.html')

def register(request):
    form = Registration()
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.save()
            login (request, user)
            return redirect ('Home')
        else:
            messages.error (request, 'Form is not correct')
    return render (request,'register.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a success page.
            # For example: return HttpResponseRedirect('/success/')
            # Replace '/success/' with your success URL.
        else:
            # Return an 'invalid login' error message.
            # For example: return render(request, 'login.html', {'error_message': 'Invalid login'})
            # Pass an error message to the template if login fails.
            return render(request, 'login.html', {'error_message': 'Invalid login'})

    return render(request, 'login.html')



@login_required
def profile_view(request):
    return render(request, 'profile.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Перенаправление на страницу входа после выхода