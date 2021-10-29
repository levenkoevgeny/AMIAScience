from django.contrib import admin
from sciencework.models import *


admin.site.register(Grif)
admin.site.register(Interest)
admin.site.register(Publisher)
admin.site.register(AuthorsInPublication)
admin.site.register(Cityforforum)
admin.site.register(Subspecies)
admin.site.register(Statuskonf)
admin.site.register(Kindkonf)
admin.site.register(Organizatorforum)
# admin.site.register(Publication)


@admin.register(Conference)
class ConferencePageAdmin(admin.ModelAdmin):
    list_display = ('id', 'conferencename', 'conferencename_short', 'forumstatus', 'kindforum', 'organizatorforum', 'forumcountry', 'forumdate')
    search_fields = ['conferencename']
    filter_horizontal = ('moderators',)


@admin.register(Publicationkind)
class PublicationkindPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'publicationkind')
    search_fields = ['publicationkind']


@admin.register(Magazine)
class PublicationMagazinePageAdmin(admin.ModelAdmin):
    list_display = ('id', 'magazinename', 'invak')
    list_display_links = ['magazinename',]
    list_filter = ('magazinename', 'invak', 'ininternational')
    filter_horizontal = ('ininternational',)


@admin.register(Digest)
class PublicationDigestPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'digestname', 'invak')
    list_display_links = ['digestname', ]
    list_filter = ('digestname', 'invak')
    filter_horizontal = ('ininternational',)


@admin.register(Publication)
class PublicationPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'outputdata', 'year')
    filter_horizontal = ('subdivisions',)
    # list_filter = ('kind__publicationkind', 'year', 'halfyear', 'sheetcount', 'subdivisions', 'authors')
    list_filter = ('year', 'forumcountry', 'kind__publicationkind')
    search_fields = ['outputdata', 'year']


@admin.register(InternationalBase)
class InternationalBasePageAdmin(admin.ModelAdmin):
    list_display = ('id', 'basename')
