from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm, EventForm, RegistrationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Event, Registration  
class User:
    def signup_view(self,request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)  # Log the user in after signup
                return redirect('dashboard')  # Redirect dashboard after signup
            else:
                print(form.errors)  # Print form errors to console for debugging
        else:
            form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form': form})

    def login_view(self,request):
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

    def logout_view(self,request):
        logout(request)
        return redirect('login')

u = User()

class dashboard:
    @login_required
    def dashboard_view(self,request):
        return render(request, 'accounts/dashboard.html')

    class CustomLoginView(LoginView):
        template_name = 'accounts/login.html'
        
    def get_success_url(self):
            next_url = self.request.POST.get('next')
            return next_url or reverse_lazy('dashboard')

    def dashboard_view(self,request):
        events = Event.objects.all()  # Get all events
        registered_events = Registration.objects.filter(user=request.user).values_list('event', flat=True)
        registered_events_details = Event.objects.filter(id__in=registered_events)

        context = {
            'events': events,
            'registered_events': registered_events_details,
        }

        return render(request, 'accounts/dashboard.html', context)

    def add_event_view(self,request):
        if request.method == 'POST':
            form = EventForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('dashboard')  
        else:
            form = EventForm()
        return render(request, 'accounts/add_event.html', {'form': form})

    def event_detail_view(self,request, event_id):
        event = get_object_or_404(Event, id=event_id)
        return render(request, 'events/event_detail.html', {'event': event})

d = dashboard()

class register:

    @login_required
    def register_for_event(self,request, event_id):
        event = get_object_or_404(Event, id=event_id)
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                registration = form.save(commit=False)
                registration.user = request.user
                registration.event = event
                registration.save()
                return redirect('dashboard')
        else:
            form = RegistrationForm()
        return render(request, 'events/register.html', {'form': form, 'event': event})

    def register_event_view(self,request, event_id):
        event = get_object_or_404(Event, id=event_id)
        
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                registration = form.save(commit=False)
                registration.event = event
                registration.user = request.user
                registration.save()
                return redirect('event_detail', event_id=event.id)
        else:
            form = RegistrationForm()
        
        return render(request, 'events/register.html', {'form': form, 'event': event})
r = register()