from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'pld'

urlpatterns = [
    path('', login_required(views.pldlist), name='list'),
    path('input/', login_required(views.inputpld), name='input'),
    path('addpld/', login_required(views.addpld), name='addpld'),
    path('update/<int:pld_id>/change', login_required(views.pldupdate), name='pldchange'),
    path('updatepld', login_required(views.pldmakeupdate), name='makeupdatepld'),
    path('delete/<pk>/delete', login_required(views.PLDDelete.as_view()), name='plddelete'),
]