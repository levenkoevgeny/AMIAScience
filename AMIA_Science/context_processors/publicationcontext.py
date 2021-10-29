from sciencework.models import *


def publcontext(request):

    return ({'publicationkindlist': Publicationkind.objects.all(),
             'griflist': Grif.objects.all(),
             'interestlist': Interest.objects.all(),
             'magazinelist': Magazine.objects.all(),
             'digestlist': Digest.objects.all(),
             'conferencelist': Conference.objects.all(),
             'publisherlist': Publisher.objects.all(),
             'internationalbaselist': InternationalBase.objects.all(),
             'subspecieslist': Subspecies.objects.all(),
             'orgfounderlist': Orgfounder.objects.all(),
             'statusforumlist': Statuskonf.objects.all(),
             'kindforumlist': Kindkonf.objects.all(),
             'orgforumlist': Organizatorforum.objects.all(),
             'cityforumlist': Cityforforum.objects.all()
             })



