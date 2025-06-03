from django.contrib import admin
from django.urls import path
from M4L2A import views

urlpatterns = [
    path('', views.main_page),

]