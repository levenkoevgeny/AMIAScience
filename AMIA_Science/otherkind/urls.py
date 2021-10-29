from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'other'

urlpatterns = [
    path('', login_required(views.otherkindlist), name='list'),
    path('input/', login_required(views.inputother), name='input'),
    path('addotherkind/', login_required(views.addotherkind), name='addotherkind'),

    path('update/<other_id>/change', login_required(views.otherupdate), name='otherchange'),
    path('updateother', login_required(views.othermakeupdate), name='makeupdateother'),
    path('delete/<pk>/delete', login_required(views.OtherDelete.as_view()), name='otherdelete'),
]