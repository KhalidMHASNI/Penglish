from django.urls import path, include
from django.contrib import admin
from . import views
from .views import GeneratePdf

app_name = 'BiLingoApp'

urlpatterns = [
    path('',views.home, name="home"),
    path('admin/', admin.site.urls),
    path('Signinup/',views.SigninupPage, name="Signinup"),
    path('index/',views.index, name="index"),
    path('formation/',views.formation),
    path('certifhtml/',views.certif),
    path('index/logout',views.logout, name="logout"),
]
