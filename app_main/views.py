from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.http import Http404

User = get_user_model()


def home_page(request):
    if not request.user.is_authenticated:
        return redirect('login')

    full_name = request.user.get_full_name()
    context = {
        "full_name": full_name,
    }

    return render(request, 'app_main/home.html', context)


def teachers(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('home')

    teachers_list = User.objects.all()

    context = {
        'teachers': teachers_list
    }

    return render(request, 'app_main/teachers.html', context)


def teacher_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if first_name and last_name and username and email and password1 and password2:
            if password1 == password2:
                user = User.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username,
                )
                user.set_password(password2)
                user.save()
                return redirect('teachers')

    return render(request, 'app_main/teacher_form.html')


def teacher_detail(request, id):
    teacher = get_object_or_404(User, id=id)
    context = {
        'teacher': teacher
    }
    return render(request, 'app_main/teacher.html', context)


def teacher_update(request, id):
    teacher = get_object_or_404(User, id=id)

    if request.method == 'POST':
        teacher.first_name = request.POST.first_name
        ...

    context = {
        'teacher': teacher
    }
    return render(request, 'app_main/teacher_form.html', context)


def teacher_delete(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('teachers')
