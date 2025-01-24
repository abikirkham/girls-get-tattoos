from django.urls import path
from . import views

urlpatterns = [
    path('', views.consultations, name='consultations'),
    path('google_login/', views.google_login, name='google_login'),
    path('google-calendar/init/', views.google_calendar_init, name='google_calendar_init'),
    path('oauth2callback/', views.google_calendar_redirect, name='google_calendar_redirect'),
    path('google-calendar/events/', views.list_events, name='list_events'),

]
