from django.contrib import admin
from reporting.models import RatingEmployee, RatingTableEmployee, RatingTableSubdivision


@admin.register(RatingEmployee)
class RatingEmployeePageAdmin(admin.ModelAdmin):
    list_display = ('id','criterion', 'value')
    search_fields = ['criterion']


@admin.register(RatingTableEmployee)
class RatingEmployeePageAdmin(admin.ModelAdmin):
    list_display = ('id','author', 'rating', 'place')
    search_fields = ['author']


@admin.register(RatingTableSubdivision)
class RatingSubdivisionPageAdmin(admin.ModelAdmin):
    list_display = ('id','subdivision', 'rating', 'place')
    search_fields = ['subdivision']