from otherkind.models import *


def otherkindcontext(request):
    return ({'сouncillist': Council.objects.all(),
             'activitylist': ActivityKind.objects.all(),
             'worklist': Work.objects.all(),
             'institutionlist': Institution.objects.all(),
             'dissertationkindlist': Dissertation_kind.objects.all(),
             'edition_name_list': Edition_name.objects.all(),
             })
