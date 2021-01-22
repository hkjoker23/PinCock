from django.contrib import admin
from django.urls import path
from accountapp.views import hello_world

app_name = "accountapp"

urlpatterns = [
    path('helloworld/', hello_world, name="hello_world"),
]
