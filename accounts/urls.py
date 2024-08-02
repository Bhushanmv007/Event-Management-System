from django.urls import path
from .views import u,d,r
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', u.signup_view, name='signup'),
    path('login/', u.login_view, name='login'),
    path('logout/', u.logout_view, name='logout'),
    path('dashboard/', d.dashboard_view, name='dashboard'),
    path('events/register/', r.register_event_view, name='register_event'),
    path('add_event/', d.add_event_view, name='add_event'),
    path('event/<int:event_id>/', d.event_detail_view, name='event_detail'),
    path('event/<int:event_id>/register/', r.register_for_event, name='register_for_event'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
