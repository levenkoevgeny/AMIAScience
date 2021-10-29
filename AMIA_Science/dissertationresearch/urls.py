from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'dissertation'

urlpatterns = [

    path('', login_required(views.dissertationlist), name='list'),
    path('input_form/', login_required(views.dissertation_input_form), name='input_form'),
    path('update_form/<dissertation_id>', login_required(views.dissertation_update_form), name='update_form'),
    path('delete/<pk>/delete',login_required(views.DissertationDelete.as_view()), name='dissertationdelete'),
]