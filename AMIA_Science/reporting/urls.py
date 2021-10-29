from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'reporting'

urlpatterns = [
    path('employee/', login_required(views.employee), name='employee'),
    path('employee_rating/', login_required(views.employee_rating), name='employee_rating'),
    path('employee_rating_all/', login_required(views.employee_rating_table), name='employee_rating_all'),
    path('subdivision_rating/', login_required(views.subdivision_rating), name='subdivision_rating'),
    path('subdivision_rating_all/', login_required(views.subdivision_rating_table), name='subdivision_rating_all'),
    path('subdivision/', login_required(views.subdivision), name='subdivision'),
    path('effectivenessnid/', login_required(views.effectivenessnid), name='effectivenessnid'),
    path('magazines/', login_required(views.magazines), name='magazines'),
    path('sciencetific_activities/', login_required(views.sciencetific_activities), name='sciencetific_activities'),
]