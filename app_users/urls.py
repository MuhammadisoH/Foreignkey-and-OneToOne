from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # path('login/', LoginView.as_view(template_name='app_users/login.html'), name='login'),
    path('registration/', views.user_registration, name='registration'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
