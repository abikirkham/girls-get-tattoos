from django.shortcuts import redirect
from django.conf import settings
from google_auth_oauthlib.flow import Flow
from django.shortcuts import redirect
from django.conf import settings
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from django.shortcuts import redirect
from django.conf import settings

def oauth2callback(request):
    state = request.session.pop("state", None)
    flow = Flow.from_client_secrets_file(
        settings.GOOGLE_CLIENT_CONFIG_FILE,
        scopes=["https://www.googleapis.com/auth/calendar.events"],
        state=state
    )
    flow.redirect_uri = settings.GOOGLE_REDIRECT_URI

    # Fetch the token using the authorization response
    authorization_response = request.build_absolute_uri()
    flow.fetch_token(authorization_response=authorization_response)

    # Store the credentials in session
    credentials = flow.credentials
    request.session['credentials'] = credentials_to_dict(credentials)

    return redirect('consultations')  # Redirect to the consultations page after successful login

def credentials_to_dict(credentials):
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }

def google_login(request):
    # Create the OAuth flow object from the client secret file
    flow = Flow.from_client_secrets_file(
        settings.GOOGLE_CLIENT_CONFIG_FILE,
        scopes=["https://www.googleapis.com/auth/calendar.events"]
    )
    flow.redirect_uri = settings.GOOGLE_REDIRECT_URI

    # Generate the authorization URL
    authorization_url, state = flow.authorization_url(
        access_type="offline", include_granted_scopes="true"
    )

    # Save the state in session to prevent CSRF attacks
    request.session["state"] = state

    return redirect(authorization_url)

# View to handle redirect to the Google Calendar booking page
def consultations(request):
    # Check if the user has already authenticated with Google
    if 'credentials' not in request.session:
        return redirect('google_login')  # Redirect to Google login page if credentials are not available
    
    # Redirect to the Google Calendar's OAuth2 callback (the booking page)
    return redirect(settings.GOOGLE_REDIRECT_URI)
