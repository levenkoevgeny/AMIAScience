from django.contrib import admin
from .models import *


admin.site.register(Researchkind)
admin.site.register(Researchstatus)
admin.site.register(Researchplace)
admin.site.register(Reason)
admin.site.register(Dissertationresearch)
	
# @admin.register(Dissertationresearch)
# class DissertationresearchPageAdmin(admin.ModelAdmin):
#     list_display = (
#         'kind',
#         'status',
#         'datebegin',
#         'dateend',
#         'dissertationtheme',
#         'reason',
#         'result',
#         'otherauthor',
#         'author',
#         'leadersemployees',
#         'leadersnotemployees',
#         'researchplace',
#         'researchplacesubdivision'
#     )
#     search_fields = ['dissertationtheme']
