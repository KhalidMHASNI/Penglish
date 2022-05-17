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
    path('certifhtml/',views.certif),
    path('index/logout',views.logout, name="logout"),
    path('api/get-quiz/', views.get_quiz , name="get_quiz"),
    path('pdf/',views.some_view),
    path('certifpdf/', GeneratePdf.as_view())
]
