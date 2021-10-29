from django.shortcuts import render
from django.http import Http404
from .models import *
from authors.models import Author, OtherAuthor
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from authors.models import Academicdegree, Academicrank
import ast
from django.db.models import Q
from authors.models import Author
from django.core.paginator import Paginator
from .filters import NIR_Filter
from django.db import transaction
from django.views.decorators.cache import cache_page


def nirlist(request):
    f = NIR_Filter(request.GET, queryset=NIR.objects.all().order_by('-id'))
    paginator = Paginator(f.qs, 50)
    page = request.GET.get('page')
    nirs = paginator.get_page(page)
    return render(request, 'nir/nir_list_extends.html', {'list': nirs,
                                                         'filter': f,
                                                         })


def inputnir(request):
    return render(request, 'nir/nir_input.html')


@transaction.atomic
def addnir(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        nirtitle = request.POST['nirnaimenovanie']
        startdate = request.POST['nirdatebegin']
        enddate = request.POST['nirdateend']

        if request.POST['nirdateapprove'] == '':
            approvedate = None
        else:
            approvedate = request.POST['nirdateapprove']

        reasonlist = request.POST.getlist('nirreason')

        item = request.POST['nirplanitem']

        if 'nirresult' in request.POST:
            result = Researchresults.objects.get(pk=request.POST['nirresult'])
        else:
            result = None

        leadersemployeesreq = None
        leadersemployeessubdivisionreq = None
        leaderother = None

        if 'thereis' in request.POST:
            if 'leaderisemployee' in request.POST:
                leaderother = OtherAuthor(
                    lastname=request.POST['disserleaderlastname'],
                    initials=request.POST['disserleaderinitials'],
                    academicdegree=Academicdegree.objects.get(pk=request.POST['academicdegree']),
                    academicrank=Academicrank.objects.get(pk=request.POST['academicrank']),
                    job=request.POST['disserleaderjob'],
                    position=request.POST['disserleaderposition']
                )
                leaderother.save()
                leadersemployeesreq = None
                leadersemployeessubdivisionreq = None
            else:
                leadersemployeesreq = Author.objects.get(pk=request.POST['leaderhidden'])
                leadersemployeessubdivisionreq = leadersemployeesreq.subdivision
                leaderother = None

        nir = NIR(
            nirtitle=nirtitle,
            startdate=startdate,
            enddate=enddate,
            approvedate=approvedate,
            planitem=item,
            result=result,
            leadersemployees=leadersemployeesreq,
            leadersnotemployees=leaderother,
            leadersemployeessubdivision=leadersemployeessubdivisionreq,
        )

        nir.save()

        for elem in reasonlist:
            reason = ReasonNIR.objects.get(pk=elem)
            reasonInNIR = ReasonInNIR(nir=nir, reason=reason)
            reasonInNIR.save()

        authorcountpr = request.POST['authorscount']

        for n in range(1, int(authorcountpr)+1):
            workauthor = Author.objects.get(pk=request.POST['authoridhidden' + str(n)])
            worksubdivision = workauthor.subdivision

            nir.subdivisions.add(worksubdivision)
            nir.authors.add(workauthor)
        nir.save()

        if 'organisation' in request.POST:
            organisation_list = request.POST.getlist('organisation')
            for elem in organisation_list:
                organisation = Organization.objects.get(pk=elem)
                nir.organization.add(organisation)
            nir.save()

        # if 'otherauthorscheckpld' in request.POST:
        #     authorscountother = request.POST['authorscountother']
        #     for p in range(1, int(authorscountother) + 1):
        #         other = OtherAuthor(
        #             lastname=request.POST['inputauthorsotherlastname' + str(p)],
        #             initials=request.POST['inputauthorsotherpatronymic' + str(p)],
        #         )
        #         other.save()
        #         nir.authorsother.add(other)
        # nir.save()
    return HttpResponseRedirect(reverse('nir:list'))


@transaction.atomic
def nirupdate(request, nir_id):
    try:
        obj = NIR.objects.get(pk=nir_id)
    except NIR.DoesNotExist:
        raise Http404("NIR does not exist")

    authorfirst = obj.authors.first()
    authorsrest = obj.authors.exclude(pk=authorfirst.id)


    if obj.authorsother.count() != 0:
        authorotherfirst = obj.authorsother.first()
        authorotherrest = obj.authorsother.exclude(pk=authorotherfirst.id)
    else:
        authorotherfirst = None
        authorotherrest = None

    reasonInNIRList = obj.reasoninnir_set.all()

    reasonIdList = []

    for reasonId in reasonInNIRList:
        reasonIdList.append(reasonId.reason.id)

    if obj.organization:
        organizationInNIR = obj.organization.all()
        organizationIdList = []

        for org in organizationInNIR:
            organizationIdList.append(org.id)
    else:
        organizationIdList = None

    return render(request, 'nir/nir_update_form.html', {'obj': obj,
                                                        'authorfirst': authorfirst,
                                                        'authorsrest': authorsrest,
                                                        'authorotherfirst': authorotherfirst,
                                                        'authorotherrest': authorotherrest,
                                                        'reasonIdList': reasonIdList,
                                                        'organizationIdList': organizationIdList,
                                                        })


def nirmakeupdate(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        nirreq = NIR.objects.get(pk=request.POST['nirid'])
        nirtitle = request.POST['nirnaimenovanie']
        startdate = request.POST['nirdatebegin']
        enddate = request.POST['nirdateend']


        if request.POST['nirdateapprove'] == '':
            approvedate = None
        else:
            approvedate = request.POST['nirdateapprove']

        reasonlist = request.POST.getlist('nirreason')

        item = request.POST['nirplanitem']

        if 'nirresult' in request.POST:
            result = Researchresults.objects.get(pk=request.POST['nirresult'])
        else:
            result = None

        leadersemployeesreq = None
        leadersemployeessubdivisionreq = None
        leaderother = None
        if 'thereis' in request.POST:
            if 'leaderisemployee' in request.POST:
                leaderother = OtherAuthor(
                    lastname=request.POST['disserleaderlastname'],
                    initials=request.POST['disserleaderinitials'],
                    academicdegree=Academicdegree.objects.get(pk=request.POST['academicdegree']),
                    academicrank=Academicrank.objects.get(pk=request.POST['academicrank']),
                    job=request.POST['disserleaderjob'],
                    position=request.POST['disserleaderposition']
                )
                leaderother.save()
                leadersemployeesreq = None
                leadersemployeessubdivisionreq = None
            else:
                leadersemployeesreq = Author.objects.get(pk=request.POST['leaderhidden'])
                leadersemployeessubdivisionreq = leadersemployeesreq.subdivision
                leaderother = None

        nirreq.nirtitle = nirtitle
        nirreq.startdate = startdate
        nirreq.enddate = enddate
        nirreq.approvedate = approvedate
        nirreq.planitem = item
        nirreq.result = result
        nirreq.leadersemployees = leadersemployeesreq
        nirreq.leadersnotemployees = leaderother
        nirreq.leadersemployeessubdivision = leadersemployeessubdivisionreq

        nirreq.subdivisions.clear()
        nirreq.authors.clear()
        nirreq.organization.clear()
        nirreq.authorsother.all().delete()

        nirreq.save()

        reasoninNIR = ReasonInNIR.objects.filter(nir=nirreq)
        reasoninNIR.delete()

        for elem in reasonlist:
            reason = ReasonNIR.objects.get(pk=elem)
            reasonInNIR = ReasonInNIR(nir=nirreq, reason=reason)
            reasonInNIR.save()

        authorcountpr = request.POST['authorscount']

        for n in range(1, int(authorcountpr) + 1):
            workauthor = Author.objects.get(pk=request.POST['authoridhidden' + str(n)])
            worksubdivision = workauthor.subdivision

            nirreq.subdivisions.add(worksubdivision)
            nirreq.authors.add(workauthor)

        if 'organisation' in request.POST:
            organisation_list = request.POST.getlist('organisation')
            for elem in organisation_list:
                organisation = Organization.objects.get(pk=elem)
                nirreq.organization.add(organisation)
            nirreq.save()

        # if 'otherauthorscheckpld' in request.POST:
        #     authorscountother = request.POST['authorscountother']
        #     for p in range(1, int(authorscountother) + 1):
        #         other = OtherAuthor(
        #             lastname=request.POST['inputauthorsotherlastname' + str(p)],
        #             initials=request.POST['inputauthorsotherpatronymic' + str(p)],
        #         )
        #         other.save()
        #         nirreq.authorsother.add(other)
        #
        # nirreq.save()

        return HttpResponseRedirect(reverse('nir:list'))


class NIRDelete(DeleteView):
    model = NIR
    success_url = reverse_lazy('nir:list')
