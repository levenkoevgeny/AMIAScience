from django.shortcuts import render
from authors.models import Author, Subdivision, OtherAuthor
from .models import Council, Work, Institution, ActivityKind, Otherkind, Dissertation_kind, Edition_name, Organizatorforum
from django.http import JsonResponse
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.http import Http404
from django.db import transaction
import ast
from django.db.models import Q
from authors.models import Author
from django.core.paginator import Paginator
from .filters import OtherKindFilter
from django.views.decorators.cache import cache_page


list_variables = {'activity': ActivityKind,
                  'сouncil': Council,
                  'completed_work_council': Work,
                  'institution': Institution,
                  'dissertation_kind': Dissertation_kind,
                  'defense_place': 'str',
                  'research_theme': 'str',
                  'defense_date': 'str',
                  'work_reason': 'str',
                  'work_kind': 'str',
                  'work_subcontractors': 'str',
                  'edition_name': Edition_name,
                  'founder': Organizatorforum,
                  'completed_work_editoral': Work,
                  'study_name': 'str',
                  'group_establishment': 'str',
                  'participation_result': 'str',
                  'other_year': 'str',
                  'research_institution': 'str',
                  }


def otherkindlist(request):
    f = OtherKindFilter(request.GET, queryset=Otherkind.objects.all().order_by('-id'))
    paginator = Paginator(f.qs, 50)
    page = request.GET.get('page')
    others = paginator.get_page(page)
    return render(request, 'otherkind/otherkind_list_extends.html', {'list': others,
                                                                     'filter': f,
                                                                     })


def inputother(request):
    return render(request, 'otherkind/otherkind_input.html')


def check_in_post(variable, var_value, request, dictionary_values):
    if variable in request.POST:
        if type(var_value) == str:
            dictionary_values[variable] = request.POST[variable]
        else:
            dictionary_values[variable] = var_value.objects.get(pk=request.POST[variable])
    else:
        dictionary_values[variable] = None


def addotherkind(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        dictionary_values = dict()

        for variable, var_value in list_variables.items():
            check_in_post(variable, var_value, request, dictionary_values)

        other = Otherkind(**dictionary_values)
        other.save()

        if 'aspirant_lastname' in request.POST and 'aspirant_initials' in request.POST:
            lastname = request.POST['aspirant_lastname']
            initials = request.POST['aspirant_initials']
            aspirant = OtherAuthor(lastname=lastname,
                                   initials=initials)
            aspirant.save()
        else:
            aspirant = None
        other.aspirant = aspirant
        other.save()

        authorscount = request.POST['authorscount']

        for n in range(1, int(authorscount) + 1):
            workauthor = Author.objects.get(pk=request.POST['authoridhidden' + str(n)])
            worksubdivision = workauthor.subdivision
            other.authors.add(workauthor)
            other.subdivisions.add(worksubdivision)
        other.save()

    return HttpResponseRedirect(reverse('other:list'))


def otherupdate(request, other_id):
    try:
        obj = Otherkind.objects.get(pk=other_id)
    except Otherkind.DoesNotExist:
        raise Http404("Otherkind does not exist")

    authorfirst = obj.authors.first()
    authorsrest = obj.authors.exclude(pk=authorfirst.id)

    return render(request, 'otherkind/otherkind_update_form.html', {'obj': obj,
                                                                    'authorfirst': authorfirst,
                                                                    'authorsrest': authorsrest,
                                                                    })


@transaction.atomic
def othermakeupdate(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        dictionary_values = dict()

        for variable, var_value in list_variables.items():
            check_in_post(variable, var_value, request, dictionary_values)

        otherkindreq = Otherkind.objects.filter(pk=request.POST['otherid'])
        otherkindreq.update(**dictionary_values)

        if otherkindreq.first().aspirant:
            otherkindreq.first().aspirant.delete()

        if 'aspirant_lastname' in request.POST and 'aspirant_initials' in request.POST:
            lastname = request.POST['aspirant_lastname']
            initials = request.POST['aspirant_initials']
            aspirant = OtherAuthor(lastname=lastname,
                                   initials=initials)
            aspirant.save()
        else:
            aspirant = None

        otherkindreq.update(aspirant=aspirant)

        authorscount = request.POST['authorscount']

        otherkindreq.first().authors.clear()
        otherkindreq.first().subdivisions.clear()

        for n in range(1, int(authorscount) + 1):
            workauthor = Author.objects.get(pk=request.POST['authoridhidden' + str(n)])
            worksubdivision = workauthor.subdivision
            otherkindreq.first().authors.add(workauthor)
            otherkindreq.first().subdivisions.add(worksubdivision)
        otherkindreq.update()

    return HttpResponseRedirect(reverse('other:list'))


class OtherDelete(DeleteView):
    model = Otherkind
    success_url = reverse_lazy('other:list')


class AuthorEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Author):
            return str(obj)
        return super().default(obj)

