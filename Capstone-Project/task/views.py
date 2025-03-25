from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Technician
from django.contrib.auth import authenticate, login

# Create your views here.

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('service_no')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login (request, user)
            return redirect ('login')
    form = RegistrationForm()
    return render(request, 'task/register.html', {'form': form})


