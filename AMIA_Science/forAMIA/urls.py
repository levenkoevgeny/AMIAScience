from django.urls import path
from . import views


app_name = 'forAMIA'

urlpatterns = [
    path('', views.subdivision_list, name='subdivision_list'),
    path('subdivision/<subdivision_id>/', views.subdivision_page, name='subdivision_page'),
    path('subdivision/<subdivision_id>/kind/<kind_id>/works/', views.works_kind_list, name='subdivision_kind_list'),
    path('subdivision/<subdivision_id>/author/<author_id>/works/', views.works_author_list, name='subdivision_author_list'),
    path('search/', views.serch_page, name='search_page'),
]