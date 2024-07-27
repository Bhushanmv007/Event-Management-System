from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, LoginForm, EventForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Event  # Import the Event model

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            return redirect('dashboard')  # Redirect to the dashboard after successful signup
        else:
            print(form.errors)  # Print form errors to console for debugging
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    
def get_success_url(self):
        next_url = self.request.POST.get('next')
        return next_url or reverse_lazy('dashboard')

def dashboard_view(request):
    events = Event.objects.all()  # Get all events
    return render(request, 'accounts/dashboard.html', {'events': events})

def add_event_view(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to dashboard or another page after saving
    else:
        form = EventForm()
    return render(request, 'accounts/add_event.html', {'form': form})

def register_event_view(request):
    # Your registration logic here
    return render(request, 'events/register.html')