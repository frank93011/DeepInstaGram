"""uncleproject URL Configuration

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
from django.urls import path , include
from explore.views import *
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('intro', intro),
    path('test', test),
    path('Openness', Openness),
    path('Conscientiousness', Conscientiousness),
    path('Extraversion', Extraversion),
    path('Agreeableness', Agreeableness),
    path('Neuroticism', Neuroticism),
    path('realized', realized),
    path('logout', logout),
    path('register', register),
    url(r'^accounts/logout/$',logout)


]
