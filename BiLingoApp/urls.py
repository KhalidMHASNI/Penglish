import imp
from django.urls import path
from . import views

urlpatterns = [
    path('Signinup/',views.SigninupPage)
]
