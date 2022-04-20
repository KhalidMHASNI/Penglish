import imp
from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('Signinup/',views.SigninupPage),
    path('Signinup/',include('django.contrib.auth.urls')),
]
