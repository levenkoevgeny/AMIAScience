from django.contrib import admin
from .models import *


@admin.register(Developmentkind)
class DevelopmentkindPageAdmin(admin.ModelAdmin):
    list_display = ('kindtitle',)
    search_fields = ['kindtitle']


@admin.register(Introductionkind)
class IntroductionkindPageAdmin(admin.ModelAdmin):
    list_display = ('introductionkindtitle',)
    search_fields = ['introductionkindtitle']


@admin.register(Introductionorganization)
class IntroductionorganizationPageAdmin(admin.ModelAdmin):
    list_display = ('organizationname',)
    search_fields = ['organizationname']


admin.register(ANR)
class ANRPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'developmentkind',
                    'introductionkind',
                    'introductionorganization',
                    'approvedate',
                    'student',)
    search_fields = ['anrtitle']
    list_filter = ('is_student_participation',)
