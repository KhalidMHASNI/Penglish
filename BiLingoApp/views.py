from django.shortcuts import render

# Create your views here.
#"def homePage(request):
#    return render(request,'home.html')


#Sign in / up  page
def SigninupPage(request):
    return render(request, 'Signinup.html')