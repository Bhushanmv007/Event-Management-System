from django.urls import path
from .views import signup_view, login_view, logout_view,dashboard_view
from django.urls import path
from .views import  register_event_view, add_event_view,event_detail_view, register_for_event
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('events/register/', register_event_view, name='register_event'),
    path('add_event/', add_event_view, name='add_event'),
    path('event/<int:event_id>/', event_detail_view, name='event_detail'),
    path('event/<int:event_id>/register/', register_for_event, name='register_for_event'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
