from nir.models import *


def nircontext(request):
    return ({'reasonlist': ReasonNIR.objects.all(),
             'resultlist': Researchresults.objects.all(),
             'nir_organisation_list': Organization.objects.all()
             })