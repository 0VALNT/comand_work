from django.contrib.auth.models import User
from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import signup_view

urlpatterns = [
    path('register/', signup_view, name='new_user'),
    path('login/', LoginView.as_view(template_name='reglog_form.html'), name='login_user'),
    path('logout/', LogoutView.as_view(template_name='reglog_form.html'), name='logout_user'),

]
