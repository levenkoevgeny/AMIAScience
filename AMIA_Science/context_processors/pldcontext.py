from pld.models import *


def pldcontext(request):
    return ({'pldkindlist': PLDkind.objects.all(),
             'polist': PatentOwner.objects.all(),
             })
