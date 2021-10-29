from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'anr'

urlpatterns = [
    path('', login_required(views.anrlist), name='list'),
    path('add/', login_required(views.add), name='add'),
    path('update/<anr_id>/change', login_required(views.update), name='update'),
    path('delete/<pk>/delete', login_required(views.ANRDelete.as_view()), name='anrdelete'),
    path('add/getallpublajax_select2', views.getallpublajax_select2, name='getallpublajax_select2'),
    path('getallpublajax', views.getallpublajax, name='getallpublajax')
]