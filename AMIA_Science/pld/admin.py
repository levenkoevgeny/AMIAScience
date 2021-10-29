from django.contrib import admin
from .models import PLDkind, PatentOwner, PLD


@admin.register(PLDkind)
class PLDkindPageAdmin(admin.ModelAdmin):
    list_display = ('kindtitle',)
    search_fields = ['kindtitle']


# @admin.register(PLD)
# class PLDPageAdmin(admin.ModelAdmin):
#     list_display = ('kind',
#                     'pldtitle',
#                     'actionstart',
#                     'registrationdate',)
#     search_fields = ['pldtitle']


@admin.register(PatentOwner)
class POPageAdmin(admin.ModelAdmin):
    list_display = ('ownername',)
    search_fields = ['ownername']

