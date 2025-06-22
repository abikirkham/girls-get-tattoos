from django.shortcuts import redirect
from django.conf import settings
from google_auth_oauthlib.flow import Flow
from django.shortcuts import render, redirect
from django.conf import settings
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from django.http import HttpResponse, HttpResponseServerError, JsonResponse
from datetime import datetime, timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ConsultationInterestForm
from django.contrib.admin.views.decorators import staff_member_required
from .models import ConsultationInterest


@staff_member_required
def consultation_admin_view(request):
    if request.method == "POST":
        entry_id = request.POST.get("entry_id")
        try:
            entry = ConsultationInterest.objects.get(id=entry_id)
            entry.read = True
            entry.save()
            messages.success(
                request, f"Marked consultation from {entry.user} as read."
            )
        except ConsultationInterest.DoesNotExist:
            messages.error(request, "Consultation entry not found.")

        return redirect("consultation_admin")

    entries = ConsultationInterest.objects.all().order_by("-submitted_at")
    return render(
        request, "consultations/consultation_admin.html", {"entries": entries}
    )


@login_required
def express_interest(request):
    if request.method == "POST":
        form = ConsultationInterestForm(request.POST)
        if form.is_valid():
            interest = form.save(commit=False)
            interest.user = request.user
            interest.save()
            messages.success(
                request, "Your consultation interest was submitted."
            )
            return redirect("home")
    else:
        form = ConsultationInterestForm()
    return render(
        request, "consultations/consultation_interest.html", {"form": form}
    )


def list_events(request):
    credentials = Credentials(**request.session["credentials"])
    service = build("calendar", "v3", credentials=credentials)

    now = datetime.utcnow().isoformat() + "Z"
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    formatted_events = [
        {
            "summary": event.get("summary"),
            "start": event.get("start", {}).get(
                "dateTime", event.get("start", {}).get("date")
            ),
            "end": event.get("end", {}).get(
                "dateTime", event.get("end", {}).get("date")
            ),
        }
        for event in events
    ]

    return JsonResponse(formatted_events, safe=False)


def list_calendars(request):
    credentials = Credentials(**request.session["credentials"])
    service = build("calendar", "v3", credentials=credentials)

    calendar_list = service.calendarList().list().execute()
    return JsonResponse(calendar_list["items"], safe=False)

    formatted_events = [
        {
            "summary": event.get("summary"),
            "start": event.get("start", {}).get(
                "dateTime", event.get("start", {}).get("date")
            ),
            "end": event.get("end", {}).get(
                "dateTime", event.get("end", {}).get("date")
            ),
        }
        for event in events
    ]

    return JsonResponse(formatted_events, safe=False)


def google_calendar_init(request):
    flow = Flow.from_client_secrets_file(
        settings.GOOGLE_CLIENT_SECRETS_FILE,
        scopes=settings.GOOGLE_API_SCOPES,
        redirect_uri=settings.GOOGLE_REDIRECT_URI,
    )
    authorization_url, state = flow.authorization_url(
        access_type="offline", include_granted_scopes="true"
    )

    request.session["state"] = state
    return redirect(authorization_url)


def google_calendar_redirect(request):
    try:
        state = request.session["state"]

        flow = Flow.from_client_secrets_file(
            settings.GOOGLE_CLIENT_SECRETS_FILE,
            scopes=settings.GOOGLE_API_SCOPES,
            state=state,
            redirect_uri=settings.GOOGLE_REDIRECT_URI,
        )

        flow.fetch_token(authorization_response=request.build_absolute_uri())
        credentials = flow.credentials
        request.session["credentials"] = credentials_to_dict(credentials)

        return HttpResponse("Calendar integration complete.")
    except Exception as e:
        return HttpResponseServerError(f"OAuth callback failed: {str(e)}")


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
    flow = Flow.from_client_secrets_file(
        settings.GOOGLE_CLIENT_CONFIG_FILE,
        scopes=["https://www.googleapis.com/auth/calendar.events"],
    )
    flow.redirect_uri = settings.GOOGLE_REDIRECT_URI

    authorization_url, state = flow.authorization_url(
        access_type="offline", include_granted_scopes="true"
    )

    request.session["state"] = state

    return redirect(authorization_url)


def consultations(request):
    if "credentials" not in request.session:
        return redirect("google_login")

    return redirect(settings.GOOGLE_REDIRECT_URI)


def google_logout(request):
    request.session.pop("credentials", None)
    request.session.pop("state", None)
    return HttpResponse("✅ Google session cleared. Try logging in again.")


def reset_google_session(request):
    request.session.flush()
    return HttpResponse("✅ Google session reset. Now try logging in again.")
