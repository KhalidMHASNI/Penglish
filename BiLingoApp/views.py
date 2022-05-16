
import random
from django.shortcuts import redirect, render
#pre-built form utilities libraries
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import JsonResponse
from urllib3 import HTTPResponse
from .models import Profile
from .models import *
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

from django.http import HttpResponse
from django.views.generic import View
 
#importing get_template from loader
from django.template.loader import get_template
#import render_to_pdf from util.py 
from .utils import render_to_pdf 

#########################################################
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


#pdf
def some_view(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 100, "Hello world.")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='P-english-certif.pdf')

#Certificat_pdf

class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
        
        #getting the template
        pdf = render_to_pdf('certif.html')
         
         #rendering the template
        return HttpResponse(pdf, content_type='application/pdf')

#Certificat_html
def certif(request):
	return render(request,'certif.html')

#{
#	'status': True
#	'data' :[
#		{},
#	]
#}

def get_quiz(request):
	try:
		question_objs = list(Question.objects.all())
		data= []
		random.shuffle((question_objs))
		for question_obj in question_objs:

			data.append({

				"category": question_obj.category.category_name,
				"question": question_obj.question,
				"marks": question_obj.marks,
				"answers":question_obj.getanswers()
				
			})

		payload ={'status': True , 'data':data } 

		return JsonResponse(payload)



	except Exception as e:
		print(e)

	return HTTPResponse("Something went wrong")