from django.contrib import admin
from .models import *

# @admin.register(Otherkind)
# class OtherkindPageAdmin(admin.ModelAdmin):
#     list_display = ('activity',
#                     'сouncil',
#                     )
#     search_fields = ['сouncil']


@admin.register(CouncilCategory)
class CouncilCategoryPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',

                    )
    search_fields = ['category_name']


@admin.register(Council)
class CouncilPageAdmin(admin.ModelAdmin):
    list_display = ('сounciltitle', 'category',

                    )
    search_fields = ['сounciltitle']


@admin.register(Work)
class WorkPageAdmin(admin.ModelAdmin):
    list_display = ('worktitle',

                    )
    search_fields = ['worktitle']


@admin.register(Institution)
class InstitutionPageAdmin(admin.ModelAdmin):
    list_display = ('institutionname',

                    )
    search_fields = ['institutionname']


@admin.register(Dissertation_kind)
class Dissertation_kindPageAdmin(admin.ModelAdmin):
    list_display = ('kind_title',

                    )
    search_fields = ['kind_title']

@admin.register(ActivityKind)
class ActivityKindPageAdmin(admin.ModelAdmin):
    list_display = ('activitytitle',

                    )
    search_fields = ['activitytitle']


@admin.register(Edition_name)
class ActivityKindPageAdmin(admin.ModelAdmin):
    list_display = ('edition_name',

                    )
    search_fields = ['edition_name']
