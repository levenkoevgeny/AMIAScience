from dissertationresearch.models import *
from authors.models import Academicrank, Academicdegree

def dissertationresearchcontext(request):
    return ({
        'researchkindlist': Researchkind.objects.all(),
        'statuslist': Researchstatus.objects.all(),
        'subdivisionlist': Subdivision.objects.all(),
        'placelist': Researchplace.objects.all(),
        'academicranklist': Academicrank.objects.all(),
        'academicdegreelist': Academicdegree.objects.all(),
        'reasondisserlist': Reason.objects.all()
    })