from django.shortcuts import render
from .models import *
from authors.models import Academicdegree, Academicrank
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.http import Http404
import ast
from django.db.models import Q
from authors.models import Author
from django.core.paginator import Paginator
from .filters import Dissertationresearch_Filter
from .forms import DissertationResearchForm
from authors.forms import OtherAuthorForm, OtherAuthorLeaderForm
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page


def dissertationlist(request):
    f = Dissertationresearch_Filter(request.GET, queryset=Dissertationresearch.objects.all().order_by('-id'))
    paginator = Paginator(f.qs, 50)
    page = request.GET.get('page')
    anrs = paginator.get_page(page)
    return render(request, 'dissertationresearch/dissertationresearch_list_extends.html', {'list': anrs,
                                                                                           'filter': f,
                                                                                           })


def dissertation_input_form(request):
    if request.method == 'POST':
        form = DissertationResearchForm(request.POST)
        if form.is_valid():
            dissertation = form.save()
            if 'leadersemployees' in request.POST and request.POST['leadersemployees'] != '':
                dissertation.leadersemployeessubdivision = dissertation.leadersemployees.subdivision
                dissertation.save()
            return HttpResponseRedirect(reverse('dissertation:list'))
        else:
            return render(request, 'dissertationresearch/disser_input_form.html', {'form': form})
    else:
        form = DissertationResearchForm
        return render(request, 'dissertationresearch/disser_input_form.html', {'form': form})


def dissertation_update_form(request, dissertation_id):
    if request.method == 'POST':
        obj = get_object_or_404(Dissertationresearch, pk=dissertation_id)
        form = DissertationResearchForm(request.POST, instance=obj)
        if form.is_valid():
            dissertation = form.save()
            if 'leadersemployees' in request.POST and request.POST['leadersemployees'] != '':
                dissertation.leadersemployeessubdivision = dissertation.leadersemployees.subdivision
                dissertation.save()
            return HttpResponseRedirect(reverse('dissertation:list'))
        else:
            return render(request, 'dissertationresearch/disser_update_form.html', {'form': form})
    else:
        obj = get_object_or_404(Dissertationresearch, pk=dissertation_id)
        form = DissertationResearchForm(instance=obj)
        return render(request, 'dissertationresearch/disser_update_form.html', {'form': form,
                                                                                'obj': obj,
                                                                                })


class DissertationDelete(DeleteView):
    model = Dissertationresearch
    success_url = reverse_lazy('dissertation:list')


class AuthorEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Author):
            return str(obj)
        return super().default(obj)

