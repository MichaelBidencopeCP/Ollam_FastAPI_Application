from django.shortcuts import render, redirect, HttpResponse
from dotenv import load_dotenv
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated

import os


load_dotenv()

# Redirect to the frontend where it will request the jwt token from the login_logic endpoint.
def login_redirect(request):
    """
    Redirects to the Google login page.
    """
    return redirect('socialaccount_login', provider='google')


#Chagne to a drf endpoint
class TokenCreation(APIView):
    """
    Logic for handling user login after Google authentication.
    This function can be customized to handle post-login actions.
    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # Generate JWT tokens
        refresh = RefreshToken.for_user(request.user)
        # User is authenticated, redirect to a success page or dashboard
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

        