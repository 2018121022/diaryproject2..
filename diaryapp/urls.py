from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('cover/', cover, name = "cover"),
    path('index/', index, name = "index"),
    path('write/', write, name = "write"),
    path('detail/<str:diary_id>', detail, name = "detail"),
    path('update/<str:diary_id>', update, name = "update"),
    path('delete/<str:diary_id>', delete, name = "delete"),
]