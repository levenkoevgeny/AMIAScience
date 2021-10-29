from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import Http404
from authors.models import *
from .models import PLDkind, PatentOwner, PLD, PatentownerInPLD
from django.urls import reverse
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
import ast
from django.db.models import Q
from authors.models import Author
from django.core.paginator import Paginator
from .filters import PLD_Filter
from django.views.decorators.cache import cache_page


def pldlist(request):
    f = PLD_Filter(request.GET, queryset=PLD.objects.all().order_by('-id'))
    paginator = Paginator(f.qs, 50)
    page = request.GET.get('page')
    plds = paginator.get_page(page)
    return render(request, 'pld/pld_list_extends.html', {'list': plds,
                                                 'filter': f,
                                                 })


def inputpld(request):
    return render(request, 'pld/pld_input.html')


def addpld(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        kind=PLDkind.objects.get(pk=request.POST['pldkind'])
        pldname=request.POST['pldname']

        if request.POST['pldstartdate']=='':
            pldstartdate = None
        else:
            pldstartdate = request.POST['pldstartdate']

        if request.POST['pldregistrationdate']=='':
            pldregistrationdate = None
        else:
            pldregistrationdate = request.POST['pldregistrationdate']

        if request.POST['pldrequestdate']=='':
            pldrequestdate = None
        else:
            pldrequestdate = request.POST['pldrequestdate']

        if 'pldowner' in request.POST:
            list = request.POST.getlist('pldowner')
        else:
            list = None

        if 'patentnumber' in request.POST:
            patentnumberreq = request.POST['patentnumber']
        else:
            patentnumberreq = None

        authorscount=request.POST['authorscount']

        pld = PLD(
            kind=kind,
            pldtitle=pldname,
            actionstart=pldstartdate,
            registrationdate=pldregistrationdate,
            requestdate=pldrequestdate,
            panentnumber=patentnumberreq,
        )
        pld.save()

        for elem in list:
            owner = PatentOwner.objects.get(pk=elem)
            poInPLD = PatentownerInPLD(pld=pld, patentowner=owner)
            poInPLD.save()

        for n in range(1, int(authorscount) + 1):
            workauthor = Author.objects.get(pk=request.POST['authoridhidden' + str(n)])
            worksubdivision = workauthor.subdivision
            pld.authors.add(workauthor)
            pld.subdivisions.add(worksubdivision)

        if 'otherauthorscheckpld' in request.POST:
            authorscountother = request.POST['authorscountother']
            for p in range(1, int(authorscountother) + 1):
                other = OtherAuthor(
                    lastname=request.POST['inputauthorsotherlastname' + str(p)],
                    initials=request.POST['inputauthorsotherpatronymic' + str(p)],
                )
                other.save()
                pld.authorsother.add(other)
        pld.save()
    return HttpResponseRedirect(reverse('pld:list'))


def pldupdate(request, pld_id):
    try:
        obj = PLD.objects.get(pk=pld_id)
    except PLD.DoesNotExist:
        raise Http404("PLD does not exist")

    patentownerinpldlist = obj.patentownerinpld_set.all()

    polist = []

    for po in patentownerinpldlist:
        polist.append(po.patentowner.id)

    authorfirst = obj.authors.first()
    authorsrest = obj.authors.exclude(pk=authorfirst.id)

    if obj.authorsother.count() != 0:
        authorotherfirst = obj.authorsother.first()
        authorotherrest = obj.authorsother.exclude(pk=authorotherfirst.id)
    else:
        authorotherfirst = None
        authorotherrest = None

    return render(request, 'pld/pld_update_form.html', {'obj': obj,
                                                        'authorfirst': authorfirst,
                                                        'authorsrest': authorsrest,
                                                        'authorotherfirst': authorotherfirst,
                                                        'authorotherrest': authorotherrest,
                                                        'poinpldlist': polist,
                                                        })


def pldmakeupdate(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pldreq = PLD.objects.get(pk=request.POST['pldid'])
        kind = PLDkind.objects.get(pk=request.POST['pldkind'])
        pldname = request.POST['pldname']

        if request.POST['pldstartdate']=='':
            pldstartdate = None
        else:
            pldstartdate = request.POST['pldstartdate']

        if request.POST['pldregistrationdate']=='':
            pldregistrationdate = None
        else:
            pldregistrationdate = request.POST['pldregistrationdate']

        if request.POST['pldrequestdate']=='':
            pldrequestdate = None
        else:
            pldrequestdate = request.POST['pldrequestdate']

        if 'pldowner' in request.POST:
            list = request.POST.getlist('pldowner')
        else:
            list = None

        if 'patentnumber' in request.POST:
            patentnumberreq = request.POST['patentnumber']
        else:
            patentnumberreq = None

        authorscount = request.POST['authorscount']

        pldreq.kind = kind
        pldreq.pldtitle = pldname
        pldreq.actionstart = pldstartdate
        pldreq.registrationdate = pldregistrationdate
        pldreq.requestdate = pldrequestdate
        pldreq.panentnumber = patentnumberreq

        poinpubl = PatentownerInPLD.objects.filter(pld=pldreq)
        poinpubl.delete()

        for elem in list:
            owner = PatentOwner.objects.get(pk=elem)
            poInPLD = PatentownerInPLD(pld=pldreq, patentowner=owner)
            poInPLD.save()

        pldreq.subdivisions.clear()
        pldreq.authors.clear()
        pldreq.authorsother.all().delete()

        for n in range(1, int(authorscount) + 1):
            workauthor = Author.objects.get(pk=request.POST['authoridhidden' + str(n)])
            worksubdivision = workauthor.subdivision
            pldreq.authors.add(workauthor)
            pldreq.subdivisions.add(worksubdivision)

        if 'otherauthorscheckpld' in request.POST:
            authorscountother = request.POST['authorscountother']
            for p in range(1, int(authorscountother) + 1):
                other = OtherAuthor(
                    lastname=request.POST['inputauthorsotherlastname' + str(p)],
                    initials=request.POST['inputauthorsotherpatronymic' + str(p)],
                )
                other.save()
                pldreq.authorsother.add(other)

        pldreq.save()
    return HttpResponseRedirect(reverse('pld:list'))


class PLDDelete(DeleteView):
    model = PLD
    success_url = reverse_lazy('pld:list')
