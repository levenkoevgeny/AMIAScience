from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import Http404
from .models import ANR, Developmentkind, Introductionorganization, Introductionkind
from nir.models import NIR
from dissertationresearch.models import Dissertationresearch
from sciencework.models import Publication
from authors.models import Author, OtherAuthor
from django.urls import reverse
from django.urls import reverse_lazy
from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic.edit import DeleteView
from django.http import JsonResponse
from django.core.serializers import serialize
from django.db import transaction
from authors.models import Author
from django.core.paginator import Paginator
from .filters import ANR_Filter
from .forms import ANRForm
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page


def anrlist(request):
    f = ANR_Filter(request.GET, queryset=ANR.objects.all().order_by('-id'))
    paginator = Paginator(f.qs, 50)
    page = request.GET.get('page')
    anrs = paginator.get_page(page)
    return render(request, 'anr/anr_list_extends.html', {'list': anrs,
                                                         'filter': f,
                                                         })


@transaction.atomic
def add(request):
    if request.method == 'POST':
        form = ANRForm(request.POST)

        if int(request.POST['developmentkind']) == 2 and 'development_has_not_base' not in request.POST:
            if request.POST['workinputhidden'] == '':
                return render(request, 'anr/anr_input_extends.html', {'form': form,
                                                                      'error_message': 'Выберите работу!!!!',})
        if form.is_valid():
            anr = form.save()
            if int(request.POST['developmentkind']) == 2 and 'development_has_not_base' not in request.POST:
                anr.sciencework = Publication.objects.get(pk=request.POST['workinputhidden'])
            for author in anr.authors.all():
                subdivision = author.subdivision
                anr.subdivisions.add(subdivision)
            anr.save()
            return HttpResponseRedirect(reverse('anr:list'))
        else:
            return render(request, 'anr/anr_input_extends.html', {'form': form})
    else:
        form = ANRForm()
        return render(request, 'anr/anr_input_extends.html', {'form': form})


@transaction.atomic
def update(request, anr_id):
    if request.method == 'POST':
        form = ANRForm(request.POST)
        if int(request.POST['developmentkind']) == 2 and 'development_has_not_base' not in request.POST:
            if request.POST['workinputhidden'] == '':
                obj = get_object_or_404(ANR, pk=request.POST['id'])
                return render(request, 'anr/anr_update_extends.html', {'form': form,
                                                                       'error_message': 'Выберите работу!!!!',
                                                                       'obj': obj,
                                                                       })
        if form.is_valid():
            anr = get_object_or_404(ANR, pk=anr_id)


            form = ANRForm(request.POST, instance=anr)
            form.save()

            if int(request.POST['developmentkind']) == 2 and 'development_has_not_base' not in request.POST:
                anr.sciencework = Publication.objects.get(pk=request.POST['workinputhidden'])

            anr.subdivisions.clear()
            for author in anr.authors.all():
                subdivision = author.subdivision
                anr.subdivisions.add(subdivision)
            anr.save()
            return HttpResponseRedirect(reverse('anr:list'))
        else:
            return render(request, 'anr/anr_update_extends.html', {'form': form})
    else:
        obj = get_object_or_404(ANR, pk=anr_id)
        form = ANRForm(instance=obj)
        return render(request, 'anr/anr_update_extends.html', {'form': form,
                                                               'obj': obj,
                                                               })


class ANRDelete(DeleteView):
    model = ANR
    success_url = reverse_lazy('anr:list')


def getallpublajax_select2(request):
    if request.method == 'GET':
        if 'search' in request.GET:
            print(request.GET['search'])
            return JsonResponse(
                serialize('json', Publication.objects.filter(outputdata__icontains=request.GET['search']), cls=PublicationEncoder),
                safe=False)
        else:
            return JsonResponse(dict())
    elif request.method == 'POST':
        pass


def getallpublajax(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        return JsonResponse(serialize('json', Publication.objects.filter(outputdata__icontains=request.POST['publinput']), cls=PublicationEncoder),safe=False)


class NIREncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, NIR):
            return str(obj)
        return super().default(obj)


class PublicationEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Publication):
            return str(obj)
        return super().default(obj)


class DissertationEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Dissertationresearch):
            return str(obj)
        return super().default(obj)