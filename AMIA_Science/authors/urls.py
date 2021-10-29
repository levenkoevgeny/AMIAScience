from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'authors'

urlpatterns = [
    path('', login_required(views.authorslist), name='list'),
    path('input/', login_required(views.inputauthorform), name='input'),

    path('addauthor/', login_required(views.addauthor), name='addauthor'),
    path('other_author_input_form/', login_required(views.other_author_input_form), name='other_author_input_form'),
    path('other_leader_input_form/', login_required(views.other_leader_input_form), name='other_leader_input_form'),
    path('input/getallauthorsajaxforcheck', views.getallauthorsajaxforcheck, name='getallauthorsajaxforcheck'),

    path('update/update/<pk>/change', login_required(views.AuthorUpdate.as_view()), name='authorchange'),
    path('delete/<pk>/', login_required(views.AuthorDelete.as_view()), name='authordelete'),
]
