from django.shortcuts import render, redirect



def login_redirect(request):
    """
    Redirects to the Google login page.
    """
    return redirect('socialaccount_login', provider='google')