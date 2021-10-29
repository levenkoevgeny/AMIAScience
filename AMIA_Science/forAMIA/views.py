from django.shortcuts import render, get_object_or_404
from authors.models import Subdivision, Author
from sciencework.models import Publication, AuthorsInPublication
from nir.models import NIR
from pld.models import PLD
from dissertationresearch.models import Dissertationresearch
from django.http import HttpResponse
from .models import VisitCounter


def subdivision_list(request):
    request_url = request.path
    counter, created = VisitCounter.objects.get_or_create(url_name=request_url)
    counter.visit_count = counter.visit_count + 1
    counter.save()
    list = Subdivision.objects.filter(subdivisionname__startswith='кафедра')
    return render(request, 'forAMIA/subdivision_list.html', {'list': list})


def subdivision_page(request, subdivision_id):
    subdivision = get_object_or_404(Subdivision, pk=subdivision_id)
    return render(request, 'forAMIA/subdivision_page.html', {'subdivision': subdivision,
                                                             })


def works_kind_list(request, subdivision_id, kind_id):
    subdivision = get_object_or_404(Subdivision, pk=subdivision_id)
    if kind_id == '1':
        work_list = Publication.objects.filter(subdivisions=subdivision)
        return render(request, 'forAMIA/work_list.html', {'subdivision_works_list': work_list,
                                                          })
    elif kind_id == '2':
        work_list = NIR.objects.filter(subdivisions=subdivision)
        return render(request, 'forAMIA/work_list.html', {'subdivision_works_list': work_list,
                                                          })
    elif kind_id == '3':
        work_list = PLD.objects.filter(subdivisions=subdivision)
        return render(request, 'forAMIA/work_list.html', {'subdivision_works_list': work_list,
                                                          })
    elif kind_id == '4':
        work_list = Dissertationresearch.objects.filter(researchplacesubdivision=subdivision)
        return render(request, 'forAMIA/work_list.html', {'subdivision_works_list': work_list,
                                                          })
    else:
        return HttpResponse("This kind not exists!!!")


def works_author_list(request, subdivision_id, author_id):
    author = get_object_or_404(Author, pk=author_id)
    work_list = Publication.objects.filter(authors=author)
    return render(request, 'forAMIA/work_list.html', {'author_works_list': work_list, })


def serch_page(request):
    return render(request, 'forAMIA/search_page.html')
