from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'BiLingoApp'

urlpatterns = [
    path('',views.home),
    path('admin/', admin.site.urls),
    path('Signinup/',views.SigninupPage, name="Signinup"),
    path('Signinup/index',views.formation),
    path('logout/',views.logout),
]
