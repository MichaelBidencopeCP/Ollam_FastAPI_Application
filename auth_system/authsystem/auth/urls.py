

from django.urls import path, include
from auth.views import login_redirect

urlpatterns = [
    path('login/', login_redirect , name='login_redirect'),
]