"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<str:name>/',views.hello),
    path('poll_q/',views.poll_q,name="poll_q"),
    path('poll/y/',views.submit,name='submit'),
    path('admin_page/',views.admin_page,name='admin_page'),
    path('login/',LoginView.as_view(template_name='myapp/login.html'),name="login"),
    path('logout/',LogoutView.as_view(template_name='myapp/index.html'),name='logout'),
    path('register/',views.register,name='register'),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('view/<str:name>/',views.view,name='view'),
    path('poll/r/',views.rating,name='rating'),
    path('poll/a/',views.ans,name='ans'),
    path('ansorrate/<str:name>/',views.ansorrate,name='ansorrate'),
    path('help/',views.help,name="help"),
    path('covid_check/',views.covid_check,name="covid_check"),
    path('covid/',views.covid_func,name="covid_func"),
    path('covid_intro/',views.covid_intro,name="covid_intro"),
]
