"""pec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include,re_path
from . import views

urlpatterns = [
    path('',views.home),
    path('services/csignup',views.csignup),
    path('services/psignup',views.psignup),
    path('services/dsignup',views.msignup),
    path('services/detail',views.msignup),
    path('services',views.server_list),
    path('services/clist',views.Carpenter_list),
    path('services/plist',views.Plumber_list),
    path('services/colist',views.Cook_list),
    path('services/cllist',views.Cleaner_list),
    path('services/elist',views.Electrician_list),
    path('services/nlist',views.Nurse_list),
    path('services/mlist',views.Mason_list),
    path('services/dlist',views.Driver_list),
    path('services/userform',views.user),
    path('services/clist/filter',views.filter),


]
