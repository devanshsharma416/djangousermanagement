from django.contrib.auth import login,authenticate
from .forms import CustomerCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')


def register(request):
    if request.method == 'GET':
        context = {
            'form': CustomerCreationForm
        }
        
        return render(request, 'register.html', context)
    elif request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.info(request, 'You have succesfully logged in')
            return redirect(reverse('dashboard'))


