from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.views.generic import CreateView



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login_user')
    else:
        form = SignUpForm()
    return render(request, 'reglog_form.html', {'form': form})