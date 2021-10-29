from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.urls import reverse
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.core.serializers.json import DjangoJSONEncoder
import ast
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import PublicationForm, ConferenceForm
from django.shortcuts import get_object_or_404
from django.db import transaction
from .filters import ScienceWork_Filter, Conference_Filter
from django.db.models import Q
from django.db.models import Sum
from django.views.decorators.cache import cache_page


def scienceworklist(request):
    f = ScienceWork_Filter(request.GET, queryset=Publication.objects.all().order_by('-id'))
    paginator = Paginator(f.qs, 50)
    page = request.GET.get('page')
    scienceworks = paginator.get_page(page)
    sheetcount_sum = 0
    for p in f.qs:
        if p.sheetcount:
            sheetcount_sum = sheetcount_sum + float(p.sheetcount)
    return render(request, 'sciencework/publication_list_extends.html', {'list': scienceworks,
                                                                         'filter': f,
                                                                         'sheetcount_sum': round(sheetcount_sum, 2),
                                                                         })


@transaction.atomic
def add(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            publication = form.save()
            if publication.magazine != None:
                publication.invak=publication.magazine.invak
                for international in publication.magazine.ininternational.all():
                    publication.ininternationals.add(international)
            elif publication.digest != None:
                publication.invak=publication.digest.invak
                for international in publication.digest.ininternational.all():
                    publication.ininternationals.add(international)
            else:
                publication.invak=False
            authorcountpr = request.POST['authorscount']
            if 'scienceworkforeignauthorscount' in request.POST:
                workforeignauthorscount = request.POST['scienceworkforeignauthorscount']
            else:
                workforeignauthorscount = 0
            publication.authorcount = int(authorcountpr) + int(workforeignauthorscount)
            publication.save()

            for n in range(1, int(authorcountpr) + 1):
                workauthor = Author.objects.get(pk=request.POST['authoridhidden' + str(n)])
                worksubdivision = workauthor.subdivision
                if 'checkboxextraauthors' + str(n) in request.POST:
                    isauthorcheck = True
                else:
                    isauthorcheck = False
                publication.subdivisions.add(worksubdivision)
                publication.save()
                authorsinpubl = AuthorsInPublication(author=workauthor, publication=publication, isauthor=isauthorcheck)
                authorsinpubl.save()
            return HttpResponseRedirect(reverse('sciencework:list'))
        else:
            return render(request, 'sciencework/scienceork_input_form.html', {'form': form})
    else:
        form = PublicationForm()
        return render(request, 'sciencework/scienceork_input_form.html', {'form': form})


@transaction.atomic
def update(request, publication_id):
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            publication = get_object_or_404(Publication, pk=publication_id)
            form = PublicationForm(request.POST, instance=publication)
            form.save(commit=False)
            publication.ininternationals.clear()
            if publication.magazine != None:
                publication.invak=publication.magazine.invak
                for international in publication.magazine.ininternational.all():
                    publication.ininternationals.add(international)
            elif publication.digest != None:
                publication.invak=publication.digest.invak
                for international in publication.digest.ininternational.all():
                    publication.ininternationals.add(international)
            else:
                publication.invak=False
            authorcountpr = request.POST['authorscount']
            if 'scienceworkforeignauthorscount' in request.POST:
                workforeignauthorscount = request.POST['scienceworkforeignauthorscount']
            else:
                workforeignauthorscount = 0
            publication.authorcount = int(authorcountpr) + int(workforeignauthorscount)

            publication.subdivisions.clear()
            authorsinpubl = AuthorsInPublication.objects.filter(publication=publication)
            authorsinpubl.delete()
            publication = form.save()
            for n in range(1, int(authorcountpr) + 1):
                workauthor = Author.objects.get(pk=request.POST['authoridhidden' + str(n)])
                worksubdivision = workauthor.subdivision
                if 'checkboxextraauthors' + str(n) in request.POST:
                    isauthorcheck = True
                else:
                    isauthorcheck = False
                publication.subdivisions.add(worksubdivision)
                publication.save()
                authorsinpubl = AuthorsInPublication(author=workauthor, publication=publication, isauthor=isauthorcheck)
                authorsinpubl.save()
            return HttpResponseRedirect(reverse('sciencework:list'))
        else:
            return render(request, 'sciencework/sciencework_update_form.html', {'form': form})
    else:
        publication = get_object_or_404(Publication, pk=publication_id)
        authorfirst = publication.authorsinpublication_set.first()
        if authorfirst is not None:
            authorsrest = publication.authorsinpublication_set.exclude(pk=authorfirst.id)
        else:
            authorsrest = None
        foreigncount = publication.authorcount - publication.authors.all().count()
        form = PublicationForm(instance=publication)
        return render(request, 'sciencework/sciencework_update_form.html', {'form': form,
                                                                            'publication': publication,
                                                                            'authorfirst': authorfirst,
                                                                            'authorsrest': authorsrest,
                                                                            'foreigncount': foreigncount,
                                                                            })


class ScienceworkDelete(DeleteView):
    model = Publication
    success_url = reverse_lazy('sciencework:list')


class AuthorEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Author):
            return str(obj)
        return super().default(obj)


def conference_list(request):
    f = Conference_Filter(request.GET, queryset=Conference.objects.all().order_by('-id'))
    paginator = Paginator(f.qs, 50)
    page = request.GET.get('page')
    conferences = paginator.get_page(page)
    return render(request, 'sciencework/conference/conference_list_extends.html', {'list': conferences,
                                                                                   'filter': f,
                                                                                   })


@transaction.atomic
def conference_add(request):
    if request.method == 'POST':
        form = ConferenceForm(request.POST)
        if form.is_valid():
            conference = form.save()
            return HttpResponseRedirect(reverse('sciencework:conference_list'))
        else:
            return render(request, 'sciencework/conference/conference_input.html', {'form': form})
    else:
        form = ConferenceForm()
        return render(request, 'sciencework/conference/conference_input.html', {'form': form})


@transaction.atomic
def conference_update(request, conference_id):
    if request.method == 'POST':
        obj = get_object_or_404(Conference, pk=conference_id)
        form = ConferenceForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('sciencework:conference_list'))
        else:
            return render(request, 'sciencework/conference/conference_update.html', {'form': form,
                                                                                     'obj': obj,
                                                                                     })

    else:
        obj = get_object_or_404(Conference, pk=conference_id)

        form = ConferenceForm(instance=obj)
        return render(request, 'sciencework/conference/conference_update.html', {'form': form,
                                                                                 'obj': obj,
                                                                                 })


class СonferenceDelete(DeleteView):
    model = Conference
    template_name = 'sciencework/conference/conference_confirm_delete.html'
    success_url = reverse_lazy('sciencework:conference_list')

