from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
#"def homePage(request):
#    return render(request,'home.html')


#Sign in / up  page
def SigninupPage(request):
	return render(request, 'Signinup.html'),
