from django.contrib import admin
from .models import *


admin.site.register(Subdivisiongroup)
admin.site.register(Subdivision)
admin.site.register(Position)
admin.site.register(Candidatespecialty)
admin.site.register(Doctorspecialty)
admin.site.register(Rank)
admin.site.register(Academicrank)
admin.site.register(Academicdegree)
admin.site.register(Workstatus)


@admin.register(Author)
class AuthorPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'lastname', 'firstname', 'patronymic',
                    'dateofbirth',
                    'position',
                    'positiondate',
                    'subdivision',
                    'isdocentvak',
                    'isprofessor',
                    'iscandidate',
                    'isdoctor',
                    'extradata',
                    'workstatus')
    search_fields = ['lastname']


@admin.register(OtherAuthor)
class AuthorOtherPageAdmin(admin.ModelAdmin):
    list_display = ('lastname',
                    # 'firstname',
                    # 'patronymic'
                    # 'position',
                    # 'subdivision',
                    # 'extradata',
                    # 'workstatus'
                    )
    search_fields = ['lastname']
