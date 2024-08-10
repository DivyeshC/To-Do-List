"""todoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path , include
from django.shortcuts import HttpResponse
from todolist.views import home,login,signup,add_todo,signout, delete_todo, change_todo, edit,update,about
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', home ,name='home'),
    path('login', login ,name='login'),
    path('signup', signup ,name='signup'),
    path('add_todo', add_todo),
    path('logout', signout),
    path('delete-todo/<int:id>', delete_todo),
    path('change-status/<int:id>/<str:status>', change_todo),
    path('edit/<int:id>', edit ,name='edit'),
    path('update/<int:id>',update,name='update'),
    path('about', about,name='about'),
]