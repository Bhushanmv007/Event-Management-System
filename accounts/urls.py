from django.urls import path
from .views import signup_view, login_view, logout_view,dashboard_view
from django.urls import path
from .views import  register_event_view, add_event_view

urlpatterns = [
    path('', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('events/register/', register_event_view, name='register_event'),
    path('add_event/', add_event_view, name='add_event'),
]
