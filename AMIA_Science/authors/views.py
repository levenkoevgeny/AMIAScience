from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *

from django.urls import reverse
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
import ast
from django.db.models import Q
from django.core.paginator import Paginator
from .filters import AuthorFilter
from django import forms
from .forms import OtherAuthorForm, OtherAuthorLeaderForm
from django.views.decorators.cache import cache_page


def authorslist(request):
    f = AuthorFilter(request.GET, queryset=Author.objects.filter(workstatus_id=1).order_by('lastname'))
    paginator = Paginator(f.qs, 50)
    page = request.GET.get('page')
    authors = paginator.get_page(page)
    return render(request, 'authors/authors_list_extends.html', {'list': authors,
                                                                 'filter': f,
                                                                 })


@permission_required('authors.can_add')
def inputauthorform(request):

    subdivisionlist = Subdivision.objects.all()
    positionlist = Position.objects.all()
    candidatespeclist = Candidatespecialty.objects.all()
    doctorspeclist = Doctorspecialty.objects.all()
    ranklist = Rank.objects.all()
    authorlist = Author.objects.all()
    workstatuslist = Workstatus.objects.all()

    return render(request, 'authors/author_input.html', {'subdivisionlist': subdivisionlist,
                                                         'positionlist': positionlist,
                                                         'candidatespeclist': candidatespeclist,
                                                         'doctorspeclist': doctorspeclist,
                                                         'ranklist': ranklist,
                                                         'authorlist': authorlist,
                                                         'workstatuslist': workstatuslist
                                                         })


def addauthor(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        lastname = request.POST['lastname']
        firstname = request.POST['firstname']
        patronymic = request.POST['patronymic']
        dateofbirth = request.POST['dateofbirth']
        subdivision = Subdivision.objects.get(pk=request.POST['employeesubdivision'])
        employeerank = Rank.objects.get(pk=request.POST['employeerank'])
        position = Position.objects.get(pk=request.POST['employeeposition'])
        employeedateposition = request.POST['employeedateposition']
        employeeworkstatus = Workstatus.objects.get(pk=request.POST['employeeworkstatus'])
        employeeextradata = request.POST['employeeextradata']

        if 'employeedocentcheck' in request.POST:
            isdocentvak = True
            employeedocentdate = request.POST['employeedocentdate']
        else:
            isdocentvak = False
            employeedocentdate = None

        if 'employeeprofessorcheck' in request.POST:
            isprofessor = True
            employeeprofessordate = request.POST['employeeprofessordate']
        else:
            isprofessor = False
            employeeprofessordate = None

        if 'employeecandidatecheck' in request.POST:
            iscandidate = True
            employeecandidatedate = request.POST['employeecandidatedate']
            employeecandidatetitle = request.POST['employeecandidatetitle']
            employeecandidatespecialty = request.POST['employeecandidatespecialty']
            candidspec = Candidatespecialty.objects.get(pk=employeecandidatespecialty)

        else:
            iscandidate = False
            employeecandidatedate = None
            employeecandidatetitle = None
            candidspec = None

        if 'employeedoctorcheck' in request.POST:
            isdoctor = True
            employeedoctordate = request.POST['employeedoctordate']
            employeedoctortitle = request.POST['employeedoctortitle']
            employeedoctorspecialty = request.POST['employeedoctorspecialty']
            doctcpec = Doctorspecialty.objects.get(pk=employeedoctorspecialty)
        else:
            isdoctor = False
            employeedoctordate = None
            employeedoctortitle = None
            doctcpec = None

        author = Author(
            subdivision=subdivision,
            lastname=lastname,
            firstname=firstname,
            patronymic=patronymic,
            dateofbirth=dateofbirth,
            rank=employeerank,
            position=position,
            positiondate=employeedateposition,
            isdocentvak=isdocentvak,
            docentvakdate=employeedocentdate,
            isprofessor=isprofessor,
            professordate=employeeprofessordate,
            iscandidate=iscandidate,
            candidatedate=employeecandidatedate,
            candidatetitle=employeecandidatetitle,
            candidatespecialty=candidspec,
            isdoctor=isdoctor,
            doctordate=employeedoctordate,
            doctortitle=employeedoctortitle,
            doctorspecialty=doctcpec,
            workstatus=employeeworkstatus,
            extradata=employeeextradata)
        author.save()
        return HttpResponseRedirect(reverse('authors:list'))


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['subdivision',
              'lastname',
              'firstname',
              'patronymic',
              'dateofbirth',
              'rank',
              'position',
              'positiondate',
              'isdocentvak',
              'docentvakdate',
              'isprofessor',
              'professordate',
              'iscandidate',
              'candidatedate',
              'candidatetitle',
              'candidatespecialty',
              'isdoctor',
              'doctordate',
              'doctortitle',
              'doctorspecialty',
              'extradata',
              'workstatus']
    template_name_suffix = '_update_form'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['dateofbirth'].widget = forms.DateInput(format=('%Y-%m-%d'), attrs={'type':'date'})
        form.fields['positiondate'].widget = forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'})
        form.fields['docentvakdate'].widget = forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'})
        form.fields['professordate'].widget = forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'})
        form.fields['candidatedate'].widget = forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'})
        form.fields['doctordate'].widget = forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'})
        return form

def getallauthorsajaxforcheck(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        lastnamereq = request.POST['authorlastname']
        dateofbirthreq = request.POST['dateofbirth']
        author = Author.objects.filter(lastname=lastnamereq, dateofbirth=dateofbirthreq)
        return JsonResponse(serialize('json', author, use_natural_foreign_keys=True, cls=AuthorEncoder), safe=False)


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors:list')

    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     print(self.object.subdivision)
    #     success_url = self.get_success_url()
    #     self.object.delete()
    #     return HttpResponseRedirect(success_url)


def other_author_input_form(request):
    if request.method == 'POST':
        form = OtherAuthorLeaderForm(request.POST)
        if form.is_valid():
            other_author = form.save()
            other_author.save()
            return JsonResponse({'new_id': other_author.id, 'new_lastname': other_author.lastname}, safe=False)
        else:
            error_message = "Заполните правильно форму!"
            return JsonResponse({'error': error_message}, safe=False)
    else:
        form = OtherAuthorLeaderForm
        return render(request, 'authors/other_author_input_form.html', {'leadersnotemployees_form': form})


def other_leader_input_form(request):
    if request.method == 'POST':
        form = OtherAuthorLeaderForm(request.POST)
        if form.is_valid():
            other_author = form.save()
            other_author.save()
            return JsonResponse({'new_id': other_author.id, 'new_lastname': other_author.lastname}, safe=False)
        else:
            error_message = "Заполните правильно форму!"
            return JsonResponse({'error': error_message}, safe=False)
    else:
        form = OtherAuthorLeaderForm
        return render(request, 'authors/other_leader_input_form.html', {'leadersnotemployees_form': form})


class AuthorEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Author):
            return str(obj)
        return super().default(obj)


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
