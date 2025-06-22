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
        "oauth2callback/",
        views.google_calendar_redirect,
        name="google_calendar_redirect",
    ),
    path("google-calendar/events/", views.list_events, name="list_events"),
    path(
        "google-calendar/calendars/",
        views.list_calendars,
        name="list_calendars",
    ),
    path("google_logout/", google_logout, name="google_logout"),
    path("reset/", views.reset_google_session, name="reset_google_session"),
    path("interest/", views.express_interest, name="consultation_interest"),
    path(
        "admin-submissions/",
        views.consultation_admin_view,
        name="consultation_admin",
    ),
]
