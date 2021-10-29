from authors.models import *


def authorscontext(request):
    return ({
        'positionlist': Position.objects.all(),
        'ranklist': Rank.objects.all(),
        'author_list': Author.objects.all(),
        'subdivision_list': Subdivision.objects.all(),
    })
