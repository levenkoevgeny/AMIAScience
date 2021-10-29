from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'nir'

urlpatterns = [
    path('', login_required(views.nirlist), name='list'),
    path('input/', login_required(views.inputnir), name='input'),
    path('addnir/', login_required(views.addnir), name='addnir'),
    path('update/<nir_id>/change', views.nirupdate, name='nirchange'),
    path('updatenir', login_required(views.nirmakeupdate), name='makeupdatenir'),
    path('delete/<pk>/delete', login_required(views.NIRDelete.as_view()), name='nirdelete'),
]