from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("",views.index , name='home' ),
    path("addgrp",views.addgroup , name='addgroup' ),
    path("contact",views.contact , name='contact' ),
    path("passbook",views.passbook , name='passbook' ),
    path('register', views.register, name="register"),
    path('login', views.loginuser, name="login"),
    path('logout', views.logoutuser, name="logout"),
    path('add', views.add ,name ='add'),
    path('addindi',views.addindi, name='addindi')
]
