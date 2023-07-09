from django.contrib import admin
from django.urls import path
from my_Form_app import views

urlpatterns = [
    path("", views.index, name='my_Form_app'),
    path("about", views.about, name='about'),
    path("form", views.form, name='form'),
    path("log", views.log, name='log'),
]