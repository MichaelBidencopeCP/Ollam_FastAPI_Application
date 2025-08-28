

from django.urls import path, include
from auth.views import login_redirect, CalendarLogic
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'calendar', CalendarLogic, basename='calendar')

urlpatterns = [
    path('login/', login_redirect , name='login_redirect'),
]

urlpatterns += router.urls
