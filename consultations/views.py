from django.shortcuts import redirect
from django.conf import settings
from google_auth_oauthlib.flow import Flow
from django.shortcuts import redirect
from django.conf import settings
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from django.shortcuts import redirect
from django.conf import settings
from googleapiclient.discovery import build
from django.http import HttpResponse


def list_events(request):
    credentials = Credentials(**request.session["credentials"])
    service = build("calendar", "v3", credentials=credentials)

    events_result = (
        service.events().list(calendarId="primary", maxResults=10).execute()
    )
    events = events_result.get("items", [])

    return HttpResponse(events)


def google_calendar_init(request):
    flow = Flow.from_client_secrets_file(
        settings.GOOGLE_CLIENT_SECRETS_FILE,
        scopes=settings.GOOGLE_API_SCOPES,
        redirect_uri=settings.REDIRECT_URI,
    )
    authorization_url, state = flow.authorization_url(
        access_type="offline", include_granted_scopes="true"
    )

    request.session["state"] = state
    return redirect(authorization_url)


def google_calendar_redirect(request):
    state = request.session["state"]

    flow = Flow.from_client_secrets_file(
        settings.GOOGLE_CLIENT_SECRETS_FILE,
        scopes=settings.GOOGLE_API_SCOPES,
        state=state,
        redirect_uri=settings.REDIRECT_URI,
    )

    flow.fetch_token(authorization_response=request.build_absolute_uri())

    credentials = flow.credentials
    request.session["credentials"] = credentials_to_dict(credentials)

    return HttpResponse(
        "Calendar integration complete. You can now use Google Calendar with your Django app."
    )


def credentials_to_dict(credentials):
    return {
        "token": credentials.token,
        "refresh_token": credentials.refresh_token,
        "token_uri": credentials.token_uri,
        "client_id": credentials.client_id,
        "client_secret": credentials.client_secret,
        "scopes": credentials.scopes,
    }


def google_login(request):
    # Create the OAuth flow object from the client secret file
    flow = Flow.from_client_secrets_file(
        settings.GOOGLE_CLIENT_CONFIG_FILE,
        scopes=["https://www.googleapis.com/auth/calendar.events"],
    )
    flow.redirect_uri = settings.GOOGLE_REDIRECT_URI

    # Generate the authorization URL
    authorization_url, state = flow.authorization_url(
        access_type="offline", include_granted_scopes="true"
    )

    # Save the state in session to prevent CSRF attacks
    request.session["state"] = state

    return redirect(authorization_url)


def consultations(request):
    if "credentials" not in request.session:
        return redirect("google_login")

    return redirect(settings.GOOGLE_REDIRECT_URI)


def oauth2callback(request):
    state = request.session["state"]

    flow = Flow.from_client_secrets_file(
        settings.GOOGLE_CLIENT_SECRETS_FILE,
        scopes=settings.GOOGLE_API_SCOPES,
        state=state,
        redirect_uri=settings.REDIRECT_URI,
    )

    flow.fetch_token(authorization_response=request.build_absolute_uri())

    credentials = flow.credentials
    request.session["credentials"] = credentials_to_dict(credentials)

    return HttpResponse(
        "Calendar integration complete. You can now use Google Calendar with your Django app."
    )


def create_event(request):
    credentials = Credentials(**request.session["credentials"])
    service = build("calendar", "v3", credentials=credentials)

    event = {
        "summary": "Tattoo Consultation",
        "start": {
            "dateTime": "2025-06-02T15:00:00",
            "timeZone": "Europe/London",
        },
        "end": {
            "dateTime": "2025-06-02T15:30:00",
            "timeZone": "Europe/London",
        },
    }

    event = service.events().insert(calendarId="primary", body=event).execute()

    return HttpResponse(f"Event created: {event.get('htmlLink')}")
