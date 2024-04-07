from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView

from .forms import UserRegistrationForm
User = get_user_model()


def user_registration(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        try:
            user = User.objects.get(email=email)
        except:
            user = None

        if password1 == password2 and not user:
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
            )
            user.set_password(password2)
            user.save()
            return redirect('login')


    form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'app_users/registration.html', context)


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user_exists = user.check_password(password)
        except:
            user_exists = None
            user = None

        if user_exists:
            login(request, user)
            return redirect('home')
    return render(request, 'app_users/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')
