from django.shortcuts import render, redirect


def home_page(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'app_main/home.html')


