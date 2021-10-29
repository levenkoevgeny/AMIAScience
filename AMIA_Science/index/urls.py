from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'index'

urlpatterns = [
    path('', login_required(views.index), name='index'),
    path('about/', login_required(views.about), name='about'),
    path('searchblock/', views.search, name='search'),
    path('getallauthorsajax', views.getallauthorsajax, name='getallauthorsajax'),
]