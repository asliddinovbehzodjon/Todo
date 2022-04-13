from django.urls import path
from .views import *
urlpatterns = [
    path('',home),
    path('register',royxatdanotish,name='register'),
    path('login',loginPage,name='login'),
    path('logout',logoutUser,name='logout')
]
