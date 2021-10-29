from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'sciencework'

urlpatterns = [
    path('', login_required(views.scienceworklist), name='list'),
    path('add/', login_required(views.add), name='add'),
    path('<publication_id>/change/', login_required(views.update), name='change'),
    path('delete/<pk>/delete/', login_required(views.ScienceworkDelete.as_view()), name='scienceworkdelete'),

    path('conference/list', views.conference_list, name='conference_list'),
    path('conference/add/', views.conference_add, name='conference_add'),
    path('conference/update/<conference_id>/change/', views.conference_update, name='conference_update'),
    path('conference/delete/<pk>/delete/', views.СonferenceDelete.as_view(), name='conference_delete'),





]