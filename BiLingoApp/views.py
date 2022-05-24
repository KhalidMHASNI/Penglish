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

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

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
			return redirect('formation')
		else :
			messages.error(request,"Password missmatchs")
			return redirect('Signinup')
	else: 
		return render(request, 'Signinup.html')

#formation page 
def formation(request):
	return render(request,'formation.html')

def logout(request):
	auth.logout(request)
	return redirect('home')

def testfinal(request):
	return render(request,'testfinal.html')
	
#change password
# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important!
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('Signinup')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'formation.html', {
#         'form': form
#     })


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

#popup
def popup(request):
	return render(request,'popup.html')

#{
#	'status': True
#	'data' :[
#		{},
#	]
#}
def pretest(request):
	context={'categories':Category.objects.all()}

	if request.GET.get('category'):
  		return redirect(f"/quiz/?category={request.GET.get('category')}")
	
	return render({request, 'quiz.html', context})


def test(request):
	context={'categories':request.GET.get('category')}
	

	return render(request, 'test.html', context)


# def get_quiz(request):
# 	try:
# 		question_objs = Question.objects.all()

# 		question_objs = question_objs.filter(category__category_name__icontains="Grammar-Conjugation-Lexicon")
# 		question_objs = list(question_objs)
# 		data= []
# 		random.shuffle(question_objs)
# 		for question_obj in question_objs:
			
# 			data.append({

# 				"category": question_obj.category.category_name,
# 				"question": question_obj.question,
# 				"marks": question_obj.marks,
# 				"answers":question_obj.getanswers()
				
# 			})

# 		payload ={'status': True , 'data':data } 

# 		return JsonResponse(payload)
# 	except Exception as e:
# 		print(e)
# 	return HTTPResponse("Something went wrong")
