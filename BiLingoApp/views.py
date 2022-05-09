
import random
from django.shortcuts import redirect, render
#pre-built form utilities libraries
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Profile

#home page 
def home(request):
	return render(request,'home.html')

#Signup  page
def SigninupPage(request):
	if request.method=='POST' and 'btnform2' in request.POST: 
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		password1 = request.POST['password']
		password2 = request.POST['cpassword']


		if password1 == password2 :
			if User.objects.filter(email=email).exists():
				messages.warning(request,'Email taken')
				return redirect('Signinup')
			else :
				myuser = User.objects.create_user(username=email, email=email,first_name=first_name,last_name=last_name ,password=password1)
				myuser.save()
				messages.success(request, "Votre compte est crée .")
				return redirect('Signinup')
		else:
			messages.info(request,'password not matching')
			return redirect('Signinup')
	if request.method== 'POST' and 'btnform1' in request.POST:
		email = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=email,password=password) 

		if user is not None:
			auth.login(request,user)
			return redirect('index')
		else :
			messages.error(request,"Password missmatchs")
			return redirect('Signinup')
	else: 
		return render(request, 'Signinup.html')


#formation page
def index(request) : 
	return render(request,'index.html')

def logout(request):
	auth.logout(request)
	return redirect('home')
