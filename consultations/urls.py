from django.urls import path
from . import views
from .views import google_logout

urlpatterns = [
    path("", views.consultations, name="consultations"),
    path("google_login/", views.google_login, name="google_login"),
    path(
        "google-calendar/init/",
        views.google_calendar_init,
        name="google_calendar_init",
    ),
    path(
        "consultations/oauth2callback/",
        views.google_calendar_redirect,
        name="google_calendar_redirect",
    ),
    path("google-calendar/events/", views.list_events, name="list_events"),
    path("google_logout/", google_logout, name="google_logout"),
]
