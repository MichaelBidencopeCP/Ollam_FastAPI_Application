from django.shortcuts import render, redirect, HttpResponse
from dotenv import load_dotenv
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated
from allauth.socialaccount.models import SocialAccount, SocialToken

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
    Logic for handling user login after Google authentication.
    This function can be customized to handle post-login actions.
    """
    if request.user.is_authenticated:
        print("User is authenticated")
        print(f"User: {request.user}")
        print(f"request:" + str(request))
        print("Social Account: " + str(SocialAccount.objects.filter(user=request.user).first()))
        print("Social Token: " + str(SocialToken.objects.filter(account__user=request.user).first()))
    return redirect('http://localhost:5173')
    

    
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

