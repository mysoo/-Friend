from django.urls import path
from .views import *
urlpatterns = [
    path('signup/', MailView.as_view())
]