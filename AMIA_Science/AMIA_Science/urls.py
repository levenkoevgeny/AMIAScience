"""AMIA_Science URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls import handler404, handler500
from authors import views as author_view

#handler404 = 'index.views.handler404'
#handler500 = 'index.views.handler500'
urlpatterns = [
    path('', include('index.urls')),
    path('author/', include('authors.urls')),
    path('sciencework/', include('sciencework.urls')),
    path('nir/', include('nir.urls')),
    path('pld/', include('pld.urls')),
    path('anr/', include('anr.urls')),
    path('other/', include('otherkind.urls')),
    path('reporting/', include('reporting.urls')),
    path('dissertation/', include('dissertationresearch.urls')),
    path('admin/', admin.site.urls),
    path('forAMIA/', include('forAMIA.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

