from django.urls import path, include
from django.contrib import admin
from . import views
from .views import GeneratePdf

app_name = 'BiLingoApp'

urlpatterns = [
    path('',views.home, name="home"),
    path('admin/', admin.site.urls),
    path('Signinup/',views.SigninupPage, name="Signinup"),
    path('formation/',views.formation, name="formation"),
    path('formation/logout',views.logout, name="logout"),

    path('formation/popup',views.popup, name="popup"),
    path('certifhtml/',views.certif),
    
    path('index/logout',views.logout, name="logout"),
    
    #certif
    path('certifhtml/',views.certif),
    path('pdf/',views.some_view),
    path('certifpdf/', GeneratePdf.as_view()),

    #test
    path('testfinal/', views.testfinal, name="testfinal"),

]
