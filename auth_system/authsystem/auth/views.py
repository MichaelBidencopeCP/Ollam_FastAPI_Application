from django.shortcuts import render, redirect, HttpResponse
from dotenv import load_dotenv
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from allauth.socialaccount.models import SocialAccount, SocialToken
import requests

import os


load_dotenv()

# Redirect to the frontend where it will request the jwt token from the login_logic endpoint.
def login_redirect(request):
    """
    Redirects to the Google login page.
    """
    return redirect('socialaccount_login', provider='google')

def login_logic(request):
    """
    Handles the login logic after Google OAuth2 authentication.
    """
    if request.user.is_authenticated:
        # If the user is already authenticated, redirect to the frontend
        return redirect('http://localhost:5173')  # Change this to your frontend URL

    # If not authenticated, redirect to the Google login page
    return redirect('socialaccount_login', provider='google')

class CalendarLogic(APIView):
    """
    Get: Retrieves the user's Google Calendar events.
    Patch: Updates the user's Google Calendar events.(not sure if I will implement this. AI creating events?)
    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            # Get the user's social account and token
            social_account = SocialAccount.objects.get(user=request.user, provider='google')
            social_token = SocialToken.objects.get(account=social_account)
            
            # Make a request to the Google Calendar API
            headers = {
                'Authorization': f'Bearer {social_token.token}',
                'Accept': 'application/json',
            }
            response = requests.get('https://www.googleapis.com/calendar/v3/calendars/primary', headers=headers)
            print(response.status_code)
            print(response.json())
            if response.status_code == 200:
                return Response(response.json())
            else:
                return Response({'error': 'Failed to retrieve calendar events'}, status=response.status_code)
        except SocialAccount.DoesNotExist:
            return Response({'error': 'Social account not found'}, status=404)
        except SocialToken.DoesNotExist:
            return Response({'error': 'Social token not found'}, status=404)
    
    
