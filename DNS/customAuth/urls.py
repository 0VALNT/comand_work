from django.contrib.auth.models import User
from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import signup_view, profile, log_out

urlpatterns = [
    path('register/', signup_view, name='new_user'),
    path('login/', LoginView.as_view(template_name='reglog_form.html'), name='login_user'),
    path('logout/', log_out, name='logout_user'),
    path('accounts/profile/', profile, name='profile')
]
