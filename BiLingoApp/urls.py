from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'BiLingoApp'

urlpatterns = [
    path('',views.home, name="home"),
    path('admin/', admin.site.urls),
    path('Signinup/',views.SigninupPage, name="Signinup"),
    path('index/',views.index, name="index"),
    path('index/logout',views.logout, name="logout"),
    path('test/',views.test, name="test"),
    path('api/get-quiz/', views.get_quiz , name="get_quiz"),
]
