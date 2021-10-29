from anr.models import *


def anrcontext(request):
    return ({
        'developmentkindlist': Developmentkind.objects.all(),
        'introductionkindlist': Introductionkind.objects.all(),
        'introductionorganizationlist': Introductionorganization.objects.all(),
    })

