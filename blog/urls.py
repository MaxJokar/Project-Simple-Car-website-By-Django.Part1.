from django.contrib import admin
from django.urls import path , include
from . import views


app_name= "blog"

urlpatterns = [

    path('', views.home , name="homepage"),
    path('electric/<slug:slug>', views.electric , name="electric"),  #http://127.0.0.1:8000/electric/Lucid
    path('aboutUs/', views.aboutUs , name="aboutUs"),
]
