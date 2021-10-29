from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authors.models import Author
from authors.views import AuthorEncoder
from django.http import JsonResponse
from django.core.serializers import serialize
from sciencework.models import Publication
from nir.models import NIR
from pld.models import PLD
from dissertationresearch.models import Dissertationresearch
from anr.models import ANR
from otherkind.models import Otherkind
from django.utils.http import is_safe_url, urlunquote
from django.http import HttpResponse


def index(request):
    return render(request, 'index/index.html')


def about(request):
    return render(request, 'index/about.html')


def search(request):
    try:
        print(request.POST['classname'])
        obj = eval(request.POST['classname'])
        keyword = request.POST['findfield']
    except Exception as exception:
        return HttpResponse('Ошибка запроса!<p><a class="nav-link" href="/">На главную</a></p>')
    fields = obj.get_search_filds(self=obj)
    list = obj.objects.none()
    for field in fields:
        lookup = "%s__icontains" % field
        query = {lookup: keyword}
        list = list | obj.objects.filter(**query)
    return render(request, request.POST['pagename'], {'list': list,
                                                      'classname': request.POST['classname'],
                                                      'pagename': request.POST['pagename']
                                                      })


def getallauthorsajax(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        lastname = request.POST['authorlastname']
        listid = (dict(request.POST)).get('idarray[]')
        listresult = Author.objects.filter(lastname__icontains=lastname)
        if listid != None:
            listresult = Author.objects.exclude(id__in=listid).filter(lastname__icontains=lastname)
        return JsonResponse(serialize('json', listresult, use_natural_foreign_keys=True, cls=AuthorEncoder), safe=False)