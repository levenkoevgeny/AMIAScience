from authors.models import Author, OtherAuthor
from sciencework.models import Publication, Conference
from nir.models import NIR
from pld.models import PLD
from dissertationresearch.models import Dissertationresearch
from anr.models import ANR
from otherkind.models import Otherkind


def counts(request):

    return {'authorcount': Author.objects.all().count(),
            'otherauthorscount': OtherAuthor.objects.all().count(),
            'publicationcount': Publication.objects.all().count(),
            'nircount': NIR.objects.all().count(),
            'pldcount': PLD.objects.all().count(),
            'discount': Dissertationresearch.objects.all().count(),
            'anrcount': ANR.objects.all().count(),
            'otherkindcount': Otherkind.objects.all().count(),
            'conference_count': Conference.objects.all().count()
            }