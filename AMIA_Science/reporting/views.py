from django.shortcuts import render, get_object_or_404
from authors.models import Author, Subdivision
from django.db.models import Q
from sciencework.models import Conference
from sciencework.models import Magazine
from nir.models import NIR
from pld.models import PLD
from anr.models import ANR
from sciencework.models import Publication, Publicationkind, PublicationSerializer, InternationalBase
from reporting.models import RatingTableEmployee, RatingTableSubdivision
from authors.models import AuthorSerializer
from docxtpl import DocxTemplate
from django.http import HttpResponse
from reporting.models import RatingEmployee
from dissertationresearch.models import Dissertationresearch
from otherkind.models import Otherkind
import datetime
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from .filters import ConferenceFilter
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page


def employee(request):
    if 'employee_id' in request.GET:
        author = get_object_or_404(Author, pk=request.GET['employee_id'])
        publicationlist = author.publication_set.all().filter(year__gte=request.GET['year_since']).filter(year__lte=request.GET['year_till']).order_by('year', 'kind__publicationkind')
        otherkind_list = author.otherkind_set.all().filter(other_year__gte=request.GET['year_since']).filter(other_year__lte=request.GET['year_till']).filter(activity_id__in=[5, 6, 7]).order_by('activity')
        nir_list_author = NIR.objects.filter(authors=author)
        nir_list_leader = NIR.objects.filter(leadersemployees=author)
        nir_list = nir_list_author.union(nir_list_leader).filter(startdate__year__lte=request.GET['year_till']).exclude(enddate__year__lt=request.GET['year_since'])
        anr_list = author.anr_set.all().filter(year__gte=request.GET['year_since']).filter(year__lte=request.GET['year_till'])
        datenow = datetime.datetime.now().date()
        date1 = author.positiondate
        delta = datenow - date1
        deltadays = delta.days
        if deltadays <= 31:
            d = deltadays
            suf = 'день(дней)'
        elif deltadays > 31 and deltadays < 365:
            d = round((deltadays/30), 1)
            suf = 'месяца(месяцев)'
        else:
            d = round((deltadays / 365), 1)
            suf = 'года(лет)'
        year_since = int(request.GET['year_since'])
        year_till = int(request.GET['year_till'])
        year_list = list()
        while year_since <= year_till:
            year_list.append(str(year_since))
            year_since = year_since+1
        return render(request, 'reporting/employee.html', {'author': author,
                                                           'publicationlist': publicationlist,
                                                           'd': d,
                                                           'suf': suf,
                                                           'year_list': year_list,
                                                           'otherkind_list': otherkind_list,
                                                           'year_till': request.GET['year_till'],
                                                           'year_since': request.GET['year_since'],
                                                           'nir_list': nir_list,
                                                           'anr_list': anr_list,
                                                           })
    else:
        return render(request, 'reporting/employee.html')


def subdivision(request):
    if 'subdivision_id' in request.GET:
        subdivision = Subdivision.objects.get(pk=request.GET['subdivision_id'])
        publication_list = subdivision.publication_set.all().filter(year__gte=request.GET['year_since']).filter(
            year__lte=request.GET['year_till']).order_by('year', 'kind__publicationkind')
        otherkind_list = subdivision.otherkind_set.all().filter(other_year__gte=request.GET['year_since']).filter(
            other_year__lte=request.GET['year_till']).filter(activity_id__in=[5, 6, 7]).order_by('activity')
        nir_list = subdivision.nir_set.all().filter(startdate__year__gte=request.GET['year_since']).filter(
            startdate__year__lte=request.GET['year_till'])
        anr_list = subdivision.anr_set.all().filter(year__gte=request.GET['year_since']).filter(
            year__lte=request.GET['year_till'])
        year_since = int(request.GET['year_since'])
        year_till = int(request.GET['year_till'])
        year_list = list()
        while year_since <= year_till:
            year_list.append(str(year_since))
            year_since = year_since + 1
        return render(request, 'reporting/subdivision_report.html', {
            'subdivision': subdivision,
            'publication_list': publication_list,
            'nir_list': nir_list,
            'anr_list': anr_list,
            'otherkind_list': otherkind_list,
            'year_till': request.GET['year_till'],
            'year_since': request.GET['year_since'],
            'year_list': year_list,
        })
    else:
        return render(request, 'reporting/subdivision_report.html')


def get_pages_count(counter_list):
    sheetcount_sum = 0
    for s_w in counter_list:
        if s_w.sheetcount:
            sheetcount_sum = sheetcount_sum + float(s_w.sheetcount)
    return round(sheetcount_sum, 2)


def effectivenessnid(request):
    if 'reportingNIDyearsince' in request.GET:
        year_since = int(request.GET.get('reportingNIDyearsince', 2021))
        year_till = int(request.GET.get('reportingNIDyeartill', year_since))
        year_list = list()
        year_since_counter = year_since
        while year_since_counter <= year_till:
            year_list.append(str(year_since_counter))
            year_since_counter = year_since_counter + 1
        publication_list = Publication.objects.all().filter(year__gte=year_since, year__lte=year_till)
        return render(request, 'reporting/effectivenessNID.html', {
            'year_list': year_list,
            'publicationlist': publication_list,
            'publicationlist_pages_count': get_pages_count(publication_list),
            'year_since': year_since,
            'year_till': year_till,
            'radio_value': request.GET.get('yearradio', 1),
        })
    else:
        return render(request, 'reporting/effectivenessNID.html')


def magazines(request):
    return render(request, 'reporting/magazines.html')


def sciencetific_activities(request):
    f = ConferenceFilter(request.GET, queryset=Conference.objects.all().order_by('-id'))
    # paginator = Paginator(f.qs, 50)
    # page = request.GET.get('page')
    conferencelist = f.qs
    return render(request, 'reporting/scientific_activities.html', {'conferencelist': conferencelist,
                                                                    'filter': f,
                                                                    })


def employee_rating(request):
    if 'employee_id' in request.GET:
        id = request.GET['employee_id']
        rating_author = get_object_or_404(Author, pk=id)
        rating = make_rating(id)

        return render(request, 'reporting/employee_rating.html',
                      {
                          'author': rating_author,
                          'rating': str(rating),
                      })
    else:
        return render(request, 'reporting/employee_rating.html')


def employee_rating_table(request):
    if request.method == 'GET':
        rating_list = RatingTableEmployee.objects.all().order_by('-rating')
        return render(request, 'reporting/employee_rating_table.html',
                      {
                          'rating_list': rating_list,
                      })
    elif request.method == 'POST':
        RatingTableEmployee.objects.all().delete()
        authors_list = Author.objects.filter(workstatus_id=1)
        for author in authors_list:
            rating_table_row = RatingTableEmployee(
                author=author,
                rating=make_rating(author.id),
                place=1,
            )
            rating_table_row.save()

        rating_list = RatingTableEmployee.objects.all().order_by('-rating')
        place = 1
        rating_row_first = rating_list.first()
        rating_row_first.place = place
        rating_row_first.save()
        rating_list_other = rating_list.exclude(author=rating_row_first.author).order_by('-rating')
        for rating_row in rating_list_other:
            if rating_row.rating != rating_row_first.rating:
                place = place + 1
                rating_row.place = place
                rating_row.save()
            else:
                rating_row.place = place
                rating_row.save()
            rating_row_first = rating_row
        rating_list = RatingTableEmployee.objects.all().order_by('place')
        return render(request, 'reporting/employee_rating_table.html',
                      {
                          'rating_list': rating_list,
                      })


def subdivision_rating(request):
    if 'subdivision_id' in request.GET:
        id = request.GET['subdivision_id']
        rating_subdivision = get_object_or_404(Subdivision, pk=id)
        rating = make_subdivision_rating(id)

        return render(request, 'reporting/subdivision_rating.html',
                      {
                          'subdivision': rating_subdivision,
                          'rating': str(rating),
                      })
    else:
        return render(request, 'reporting/subdivision_rating.html')


def subdivision_rating_table(request):
    if request.method == 'GET':
        rating_list = RatingTableSubdivision.objects.all().order_by('-rating')
        return render(request, 'reporting/subdivision_rating_table.html',
                      {
                          'rating_list': rating_list,
                      })
    elif request.method == 'POST':
        RatingTableSubdivision.objects.all().delete()
        for subdivision in Subdivision.objects.all():
            rating_table_row = RatingTableSubdivision(
                subdivision=subdivision,
                rating=make_subdivision_rating(subdivision.id),
                place=1,
            )
            rating_table_row.save()
        rating_list = RatingTableSubdivision.objects.all().order_by('-rating')
        place = 1
        rating_row_first = rating_list.first()
        rating_row_first.place = place
        rating_row_first.save()
        rating_list_other = rating_list.exclude(subdivision=rating_row_first.subdivision).order_by('-rating')
        for rating_row in rating_list_other:
            if rating_row.rating != rating_row_first.rating:
                place = place + 1
                rating_row.place = place
                rating_row.save()
            else:
                rating_row.place = place
                rating_row.save()
            rating_row_first = rating_row
        rating_list = RatingTableSubdivision.objects.all().order_by('place')
        return render(request, 'reporting/subdivision_rating_table.html',
                      {
                          'rating_list': rating_list,
                      })


def make_subdivision_rating(id):
    subdivision_rating = 0
    subdivision = get_object_or_404(Subdivision, pk=id)
    for author in subdivision.author_set.all():
        subdivision_rating = subdivision_rating + make_rating(author.id)
    try:
        author_count = subdivision.author_set.filter(workstatus_id=1).count()
        return round(subdivision_rating/author_count, 1)
    except ZeroDivisionError:
        return 0


def make_rating(id):
    rating_author = get_object_or_404(Author, pk=id)
    rating = 0
    year = RatingEmployee.objects.get(pk=1).value

    # Раздел 1 Защита диссертации

    if rating_author.candidatedate is not None:
        if rating_author.candidatedate.year == year:
            rating = rating + RatingEmployee.objects.get(pk=2).value

    if rating_author.doctordate is not None:
        if rating_author.doctordate.year == year:
            rating = rating + RatingEmployee.objects.get(pk=3).value

    # Раздел 2 Подготовка кандидата или доктора наук

    disser_list_candidate = Dissertationresearch.objects.filter(leadersemployees=rating_author).filter(
        dateprotect__year=year)

    rating = rating + RatingEmployee.objects.get(pk=4).value * disser_list_candidate.count()

    disser_list_doctor = Dissertationresearch.objects.filter(leadersemployees=rating_author).filter(
        author__isnull=False).filter(author__doctordate__year=year)
    rating = rating + RatingEmployee.objects.get(pk=5).value * disser_list_doctor.count()

    # Раздел 3 Работа в специализированных советах

    сouncil_list = Otherkind.objects.filter(activity_id=5).filter(authors=rating_author).filter(other_year=year)

    for council in сouncil_list.filter(сouncil__category_id=1):
        if council.completed_work_council_id == 1 or council.completed_work_council_id == 6:
            rating = rating + RatingEmployee.objects.get(pk=6).value
        else:
            rating = rating + RatingEmployee.objects.get(pk=7).value

    for council in сouncil_list.filter(сouncil__category_id=2):
        if council.completed_work_council_id == 1 or council.completed_work_council_id == 6:
            rating = rating + RatingEmployee.objects.get(pk=8).value
        else:
            rating = rating + RatingEmployee.objects.get(pk=9).value

    for council in сouncil_list.filter(сouncil__category_id=3):
        if council.completed_work_council_id == 1 or council.completed_work_council_id == 6:
            rating = rating + RatingEmployee.objects.get(pk=10).value
        else:
            rating = rating + RatingEmployee.objects.get(pk=11).value

    for council in сouncil_list.filter(сouncil__category_id=4):
        if council.completed_work_council_id == 1 or council.completed_work_council_id == 8:
            rating = rating + RatingEmployee.objects.get(pk=12).value
        else:
            rating = rating + RatingEmployee.objects.get(pk=13).value

    for council in сouncil_list.filter(сouncil__category_id=5):
        if council.completed_work_council_id == 1:
            rating = rating + RatingEmployee.objects.get(pk=14).value
        else:
            rating = rating + RatingEmployee.objects.get(pk=15).value

    # Раздел 4 Экспертиза

    сouncil_list_expert = Otherkind.objects.filter(Q(activity_id=4) | Q(activity_id=9)).filter(
        authors=rating_author).filter(other_year=year)

    rating = rating + сouncil_list_expert.filter(dissertation_kind_id=1).count() * RatingEmployee.objects.get(
        pk=16).value
    rating = rating + сouncil_list_expert.filter(dissertation_kind_id=2).count() * RatingEmployee.objects.get(
        pk=17).value

    # Раздел 5 Подготовка отзыва на автореферат

    сouncil_list_refer = Otherkind.objects.filter(activity_id=8).filter(
        authors=rating_author).filter(other_year=year)

    rating = rating + сouncil_list_refer.filter(dissertation_kind_id=1).count() * RatingEmployee.objects.get(
        pk=25).value
    rating = rating + сouncil_list_refer.filter(dissertation_kind_id=2).count() * RatingEmployee.objects.get(
        pk=26).value

    # Раздел 6 Участие в разработке законодательных актов, концепций и т.п.

    сouncil_list_refer = Otherkind.objects.filter(activity_id=3).filter(
        authors=rating_author).filter(other_year=year)

    rating = rating + сouncil_list_refer.count() * RatingEmployee.objects.get(pk=18).value

    # Раздел 7 ПЛД

    pld_list = PLD.objects.filter(authors=rating_author).filter(registrationdate__year=year)

    evras_list = pld_list.filter(kind_id=4)
    for evras in evras_list:
        rating = rating + RatingEmployee.objects.get(pk=19).value / evras.authors.count()

    rb_list = pld_list.filter(kind_id=2)
    for rb in rb_list:
        rating = rating + RatingEmployee.objects.get(pk=20).value / rb.authors.count()

    racional_list = pld_list.filter(kind_id=5)
    for racional in racional_list:
        rating = rating + RatingEmployee.objects.get(pk=21).value / racional.authors.count()

    programm_list = pld_list.filter(kind_id=3)
    for programm in programm_list:
        rating = rating + RatingEmployee.objects.get(pk=22).value / programm.authors.count()

    demand_list = pld_list.filter(kind_id=6)
    for demand in demand_list:
        rating = rating + RatingEmployee.objects.get(pk=23).value / demand.authors.count()

    # Раздел 8 Внедрение результатов научной деятельности

    anr_list = ANR.objects.filter(authors=rating_author).filter(year=year)

    for anr in anr_list:
        rating = rating + RatingEmployee.objects.get(pk=24).value / anr.authors.count()

    # Раздел 9 Отчет по НИР

    nir_list = NIR.objects.filter(authors=rating_author).filter(approvedate__year=year)

    for nir in nir_list:
        rating = rating + RatingEmployee.objects.get(pk=27).value / (nir.authors.count() + 1)

    # Раздел 10 Участие в составе редакционных коллегий

    colleg_list = Otherkind.objects.filter(activity_id=6).filter(authors=rating_author).filter(other_year=year)
    rating = rating + RatingEmployee.objects.get(pk=28).value * colleg_list.count()

    # Раздел 11 Участие в проведении НИР в рамках международных проектов и т.д.

    nir_list_main = NIR.objects.filter(approvedate__isnull=True).filter(Q(startdate__year__lte=year) and Q(enddate__year__gte=year))

    nir_list_leader = nir_list_main.filter(leadersemployees=rating_author)
    rating = rating + nir_list_leader.count() * RatingEmployee.objects.get(pk=41).value

    nir_list_member = nir_list_main.filter(authors=rating_author)
    rating = rating + nir_list_member.count() * RatingEmployee.objects.get(pk=42).value

    nir_list_other = Otherkind.objects.filter(activity_id=7).filter(authors=rating_author).filter(other_year=year)
    rating = rating + nir_list_other.count() * RatingEmployee.objects.get(pk=42).value


    # Раздел 12 Модератор научного форума / руководитель секции

    conference_list_international = Conference.objects.filter(moderators=rating_author).filter(forumdate__year=year).filter(forumstatus_id=2)
    rating = rating + RatingEmployee.objects.get(pk=29).value * conference_list_international.count()

    conference_list_republ = Conference.objects.filter(moderators=rating_author).filter(forumdate__year=year).filter(
        Q(forumstatus_id=1) | Q(forumstatus_id=3))
    rating = rating + RatingEmployee.objects.get(pk=30).value * conference_list_republ.count()

    # Раздел 13 Публикационная активность

    monograph_list = Publication.objects.filter(kind_id=1).filter(authors=rating_author).filter(year=year)
    for monograph in monograph_list:
        rating = rating + float(monograph.sheetcount) * RatingEmployee.objects.get(pk=31).value / monograph.authorcount

    digest_magazine_list = Publication.objects.filter(kind_id=9).filter(authors=rating_author).filter(year=year).filter(
        conference__isnull=True)

    for d_m in digest_magazine_list:
        rating = rating + RatingEmployee.objects.get(pk=44).value / d_m.authorcount

    vestnik_list = Publication.objects.filter(kind_id=9).filter(authors=rating_author).filter(year=year).filter(
        magazine_id=1)
    for vestnik in vestnik_list:
        rating = rating + RatingEmployee.objects.get(pk=32).value / vestnik.authorcount

    VAK_list = Publication.objects.filter(kind_id=9).filter(authors=rating_author).filter(year=year).filter(
        Q(magazine__invak=True) | Q(digest__invak=True))
    for vak in VAK_list:
        rating = rating + RatingEmployee.objects.get(pk=33).value / vak.authorcount

    scopus = get_object_or_404(InternationalBase, pk=1)
    scopus_list = Publication.objects.filter(Q(magazine__ininternational=scopus) | Q(digest__ininternational=scopus)).filter(authors=rating_author).filter(
        year=year)
    for scop in scopus_list:
        rating = rating + RatingEmployee.objects.get(pk=34).value / scop.authorcount

    web_of_science = get_object_or_404(InternationalBase, pk=3)
    web_of_science_list = Publication.objects.filter(Q(magazine__ininternational=web_of_science) | Q(digest__ininternational=web_of_science)).filter(
        authors=rating_author).filter(
        year=year)
    for web in web_of_science_list:
        rating = rating + RatingEmployee.objects.get(pk=35).value / web.authorcount

    rinc = get_object_or_404(InternationalBase, pk=2)
    rinc_list = Publication.objects.filter(Q(magazine__ininternational=rinc) | Q(digest__ininternational=rinc)).filter(authors=rating_author).filter(
        year=year)
    for rin in rinc_list:
        rating = rating + RatingEmployee.objects.get(pk=36).value / rin.authorcount

    google_scholar = get_object_or_404(InternationalBase, pk=4)
    google_scholar_list = Publication.objects.filter(Q(magazine__ininternational=google_scholar) | Q(digest__ininternational=google_scholar)).filter(
        authors=rating_author).filter(year=year)
    for g_s in google_scholar_list:
        rating = rating + RatingEmployee.objects.get(pk=45).value / g_s.authorcount

    periodicals_directory = get_object_or_404(InternationalBase, pk=5)
    periodicals_directory_list = Publication.objects.filter(
        Q(magazine__ininternational=periodicals_directory) | Q(digest__ininternational=periodicals_directory)).filter(
        authors=rating_author).filter(year=year)
    for p_d in periodicals_directory_list:
        rating = rating + RatingEmployee.objects.get(pk=46).value / p_d.authorcount

    digest_list = Publication.objects.filter(kind_id=9).filter(authors=rating_author).filter(year=year).filter(conference__isnull=False)

    for digest in digest_list:
        rating = rating + RatingEmployee.objects.get(pk=37).value / digest.authorcount

    thesis_list = Publication.objects.filter(authors=rating_author).filter(year=year).filter(Q(kind_id=10) | Q(kind_id=11))
    for thesis in thesis_list:
        rating = rating + RatingEmployee.objects.get(pk=38).value / thesis.authorcount

    comment_list = Publication.objects.filter(authors=rating_author).filter(year=year).filter(kind_id=8)
    for comment in comment_list:
        rating = rating + float(comment.sheetcount) * RatingEmployee.objects.get(pk=39).value / comment.authorcount

    methodological_list = Publication.objects.filter(authors=rating_author).filter(year=year).filter(kind_id=6)
    for methodological in methodological_list:
        rating = rating + float(methodological.sheetcount) * RatingEmployee.objects.get(pk=40).value / methodological.authorcount

    return rating



#
#
#
#
#
#
#
# def author_list (request):
#     doc = DocxTemplate(os.path.join(BASE_DIR,"doc_templates/author/author_list.docx"))
#     #counter = 1
#     author_list = author_list_return(request)
#     data = {"author_list":author_list, "header": "Список сотрудников, выбранных по фильтру"}
#     '''            data = {"list": [], "header": "Статистический отчет по автору " + author.lastname + " " + author.firstname + " " + author.patronymic + " за " + request.POST['reportingNIDyear'] + " год"}
#                 makecounteryear(data, author, counter, request.POST['reportingNIDyear'],
#                                 request.POST['reportingNIDyear'])'''
#     doc.render(data)
#     response = HttpResponse(
#         content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#     response['Content-Disposition'] = 'attachment; filename=author_list.docx'
#     doc.save(response)
#     return response
# def sciencework_list (request):
#     doc = DocxTemplate(os.path.join(BASE_DIR,"doc_templates/sciencework/sciencework_list.docx"))
#     #counter = 1
#     sciencework_list = sciencework_list_return(request)
#     data = {"sciencework_list":sciencework_list, "header": "Список научных работ, выбранных по фильтру"}
#     '''            data = {"list": [], "header": "Статистический отчет по автору " + author.lastname + " " + author.firstname + " " + author.patronymic + " за " + request.POST['reportingNIDyear'] + " год"}
#                 makecounteryear(data, author, counter, request.POST['reportingNIDyear'],
#                                 request.POST['reportingNIDyear'])'''
#     doc.render(data)
#     response = HttpResponse(
#         content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#     response['Content-Disposition'] = 'attachment; filename=sciencework_list.docx'
#     doc.save(response)
#     return response
#
# def nir_list (request):
#     doc = DocxTemplate(os.path.join(BASE_DIR,"doc_templates/nir/nir_list.docx"))
#     #counter = 1
#     nir_list = nir_list_return(request)
#     data = {"nir_list":nir_list, "header": "Список НИР, выбранных по фильтру"}
#     '''            data = {"list": [], "header": "Статистический отчет по автору " + author.lastname + " " + author.firstname + " " + author.patronymic + " за " + request.POST['reportingNIDyear'] + " год"}
#                 makecounteryear(data, author, counter, request.POST['reportingNIDyear'],
#                                 request.POST['reportingNIDyear'])'''
#     doc.render(data)
#     response = HttpResponse(
#         content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#     response['Content-Disposition'] = 'attachment; filename=nir_list.docx'
#     doc.save(response)
#     return response
#
# def pld_list (request):
#     doc = DocxTemplate(os.path.join(BASE_DIR,"doc_templates/pld/pld_list.docx"))
#     #counter = 1
#     pld_list = pld_list_return(request)
#     data = {"pld_list":pld_list, "header": "Список ПЛД, выбранных по фильтру"}
#     '''            data = {"list": [], "header": "Статистический отчет по автору " + author.lastname + " " + author.firstname + " " + author.patronymic + " за " + request.POST['reportingNIDyear'] + " год"}
#                 makecounteryear(data, author, counter, request.POST['reportingNIDyear'],
#                                 request.POST['reportingNIDyear'])'''
#     doc.render(data)
#     response = HttpResponse(
#         content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#     response['Content-Disposition'] = 'attachment; filename=pld_list.docx'
#     doc.save(response)
#     return response
# def dissertation_list (request):
#     doc = DocxTemplate(os.path.join(BASE_DIR,"doc_templates/dissertation/dissertation_list.docx"))
#     #counter = 1
#     dissertation_list = dissertation_list_return(request)
#     data = {"dissertation_list":dissertation_list, "header": "Список диссертационных исследований, выбранных по фильтру"}
#     '''            data = {"list": [], "header": "Статистический отчет по автору " + author.lastname + " " + author.firstname + " " + author.patronymic + " за " + request.POST['reportingNIDyear'] + " год"}
#                 makecounteryear(data, author, counter, request.POST['reportingNIDyear'],
#                                 request.POST['reportingNIDyear'])'''
#     doc.render(data)
#     response = HttpResponse(
#         content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#     response['Content-Disposition'] = 'attachment; filename=dissertation_list.docx'
#     doc.save(response)
#     return response
#
# def anr_list (request):
#     doc = DocxTemplate(os.path.join(BASE_DIR,"doc_templates/anr/anr_list.docx"))
#     #counter = 1
#     anr_list = anr_list_return(request)
#     #import pdb;pdb.set_trace()
#     data = {"anr_list":anr_list, "header": "Список АНР, выбранных по фильтру"}
#     '''            data = {"list": [], "header": "Статистический отчет по автору " + author.lastname + " " + author.firstname + " " + author.patronymic + " за " + request.POST['reportingNIDyear'] + " год"}
#                 makecounteryear(data, author, counter, request.POST['reportingNIDyear'],
#                                 request.POST['reportingNIDyear'])'''
#     doc.render(data)
#     response = HttpResponse(
#         content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#     response['Content-Disposition'] = 'attachment; filename=anr_list.docx'
#     doc.save(response)
#     return response
#
#
# def effectivenesnid(request):
#     return render(request, 'reporting/effectivenessNID.html')
#
#
# def effectivenesnidreport(request):
#     if request.method == 'GET':
#         pass
#     elif request.method == 'POST':
#         currentfolder = os.getcwd()
#         doc = DocxTemplate(os.path.join(BASE_DIR,"doc_templates/effectivenesnid.docx"))
#         if request.POST['yearradio'] == '1':
#             publicationlist = Publication.objects.filter(year=request.POST['reportingNIDyear'])
#         # data = {"repairings": [], "header": "Отчет РЕЗУЛЬТАТИВНОСТЬ НИД по видам разработок и годам"}
#         # for author in Author.objects.all():
#         #     serializer = AuthorSerializer(author)
#         #     data['repairings'].append(serializer.data)
#         #     doc.render(data)
#         response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#         response['Content-Disposition'] = 'attachment; filename=Effectivenesnid.docx'
#         doc.save(response)
#     return response
#
#
# def staticreport(request):
#     departmentlist = Subdivision.objects.all()
#     return render(request, 'reporting/staticreport.html', {'departmentlist': departmentlist})
#
#
# def staticreportmake(request):
#
#     def makecounteryear(data, entity, counter, year1, year2):
#         publicationlist = entity.publication_set.filter(Q(year__gte=year1) & Q(year__lte=year2))
#         monographcount = publicationlist.filter(kind_id=1).count()  # монографии
#         textbookcount = publicationlist.filter(kind_id=2).count()  # учебник
#         tutoriallistcount = publicationlist.filter(subspecies_id=1).count()  # учебное пособие
#         teachingaidcount = publicationlist.filter(subspecies_id=2).count()  # учебное-методическое пособие
#         aidcount = publicationlist.filter(subspecies_id=3).count()  # пособие
#         practicalaidcount = publicationlist.filter(subspecies_id=4).count()  # практикум
#         educationalvisualcount = publicationlist.filter(subspecies_id=5).count()  # учебно-наглядное пособие
#         practicalcount = publicationlist.filter(kind_id=5).count()  # практическое поособие
#         methodicaldevelopmentcount = publicationlist.filter(kind_id=6).count()  # методическая разработка
#         referenceeditioncount = publicationlist.filter(kind_id=7).count()  # справочное издание
#         commentarycount = publicationlist.filter(kind_id=8).count()  # комментарий законодательства
#         researcharticlecountnotvak = publicationlist.filter(kind_id=9).filter(
#             invak=False).count()  # научная статья не ВАК
#         researcharticlecountvak = publicationlist.filter(kind_id=9).filter(invak=True).count()  # научная статья ВАК
#         conferencecount = publicationlist.filter(kind_id=10).count()  # материалы конференции
#         thesescount = publicationlist.filter(kind_id=11).count()  # тезисы докладов
#         othercount = publicationlist.filter(kind_id=12).count()  # иная публикация
#         if isinstance(entity, Author):
#             meta = entity.lastname + ' ' + entity.firstname[0] + '.' + entity.patronymic[0] + '.'
#         elif isinstance(entity, Subdivision):
#             meta = entity.subdivisionname
#
#         data['list'].append({
#             'id': counter,
#             'meta': meta,
#             'monographcount': monographcount,
#             'textbookcount': textbookcount,
#             'tutoriallistcount': tutoriallistcount,
#             'teachingaidcount': teachingaidcount,
#             'aidcount': aidcount,
#             'practicalaidcount': practicalaidcount,
#             'educationalvisualcount': educationalvisualcount,
#             'practicalcount': practicalcount,
#             'methodicaldevelopmentcount': methodicaldevelopmentcount,
#             'referenceeditioncount': referenceeditioncount,
#             'commentarycount': commentarycount,
#             'researcharticlecountnotvak': researcharticlecountnotvak,
#             'researcharticlecountvak': researcharticlecountvak,
#             'conferencecount': conferencecount,
#             'thesescount': thesescount,
#             'othercount': othercount
#         })
#
#
#     def makecounteryearsubdiv_empl(data, entity, counter, year1, year2):
#
#         dataempl = {"listauthor": []}
#         c = 1
#         for author in entity.author_set.all():
#             publicationlist = author.publication_set.filter(Q(year__gte=year1) & Q(year__lte=year2))
#             monographcount = publicationlist.filter(kind_id=1).count()  # монографии
#             textbookcount = publicationlist.filter(kind_id=2).count()  # учебник
#             tutoriallistcount = publicationlist.filter(subspecies_id=1).count()  # учебное пособие
#             teachingaidcount = publicationlist.filter(subspecies_id=2).count()  # учебное-методическое пособие
#             aidcount = publicationlist.filter(subspecies_id=3).count()  # пособие
#             practicalaidcount = publicationlist.filter(subspecies_id=4).count()  # практикум
#             educationalvisualcount = publicationlist.filter(subspecies_id=5).count()  # учебно-наглядное пособие
#             practicalcount = publicationlist.filter(kind_id=5).count()  # практическое поособие
#             methodicaldevelopmentcount = publicationlist.filter(kind_id=6).count()  # методическая разработка
#             referenceeditioncount = publicationlist.filter(kind_id=7).count()  # справочное издание
#             commentarycount = publicationlist.filter(kind_id=8).count()  # комментарий законодательства
#             researcharticlecountnotvak = publicationlist.filter(kind_id=9).filter(
#                 invak=False).count()  # научная статья не ВАК
#             researcharticlecountvak = publicationlist.filter(kind_id=9).filter(invak=True).count()  # научная статья ВАК
#             conferencecount = publicationlist.filter(kind_id=10).count()  # материалы конференции
#             thesescount = publicationlist.filter(kind_id=11).count()  # тезисы докладов
#             othercount = publicationlist.filter(kind_id=12).count()  # иная публикация
#             meta = author.lastname + ' ' + author.firstname[0] + '.' + author.patronymic[0] + '.'
#
#             dataempl['listauthor'].append({
#                 'c': c,
#                 'meta': meta,
#                 'monographcount': monographcount,
#                 'textbookcount': textbookcount,
#                 'tutoriallistcount': tutoriallistcount,
#                 'teachingaidcount': teachingaidcount,
#                 'aidcount': aidcount,
#                 'practicalaidcount': practicalaidcount,
#                 'educationalvisualcount': educationalvisualcount,
#                 'practicalcount': practicalcount,
#                 'methodicaldevelopmentcount': methodicaldevelopmentcount,
#                 'referenceeditioncount': referenceeditioncount,
#                 'commentarycount': commentarycount,
#                 'researcharticlecountnotvak': researcharticlecountnotvak,
#                 'researcharticlecountvak': researcharticlecountvak,
#                 'conferencecount': conferencecount,
#                 'thesescount': thesescount,
#                 'othercount': othercount
#             })
#             c += 1
#
#         metasubdivision = entity.subdivisionname
#
#         data['list'].append({
#             'id': counter,
#             'metasubdivision': metasubdivision,
#             'dataempl': dataempl
#         })
#
#
#     if request.method == 'GET':
#         pass
#     elif request.method == 'POST':
#         reportkind = int(request.POST['reportkind'])
#         if int(request.POST['yearradio']) == 1:
#             if reportkind == 0:
#                 doc = DocxTemplate(os.path.join(BASE_DIR,"doc_templates/staticreport/statisticreportallemployees.docx"))
#                 counter = 1
#                 author = Author.objects.get(pk = request.POST['authoridhidden1'])
#                 data = {"list": [], "header": "Статистический отчет по автору " + author.lastname + " " + author.firstname + " " + author.patronymic + " за " + request.POST['reportingNIDyear'] + " год"}
#                 makecounteryear(data, author, counter, request.POST['reportingNIDyear'],
#                                 request.POST['reportingNIDyear'])
#                 doc.render(data)
#                 response = HttpResponse(
#                     content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#                 response['Content-Disposition'] = 'attachment; filename=Statisticreportallempl.docx'
#                 doc.save(response)
#                 return response
#
#             elif reportkind == 1:
#                 doc = DocxTemplate(os.path.join(BASE_DIR,"doc_templates/staticreport/statisticreportallemployees.docx"))
#                 counter = 1
#                 subdivision = Subdivision.objects.get(pk = request.POST['department'])
#                 data = {"list": [], "header": "Статистический отчет по " + subdivision.subdivisionname + " за " + request.POST['reportingNIDyear'] + " год"}
#                 makecounteryear(data, subdivision, counter, request.POST['reportingNIDyear'],
#                                 request.POST['reportingNIDyear'])
#                 doc.render(data)
#                 response = HttpResponse(
#                     content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#                 response['Content-Disposition'] = 'attachment; filename=Statisticreportallempl.docx'
#                 doc.save(response)
#                 return response
#
#             elif reportkind == 2:
#                 doc = DocxTemplate(os.path.join(BASE_DIR,"doc_templates/staticreport/statisticreportallemployees.docx"))
#                 authorlist = Author.objects.all()
#                 data = {"list": [], "header": "Статистический отчет по сотрудникам" + " за " + request.POST['reportingNIDyear'] + " год"}
#                 counter = 1
#                 for author in authorlist:
#                     makecounteryear(data, author, counter, request.POST['reportingNIDyear'], request.POST['reportingNIDyear'])
#                     counter+=1
#                 doc.render(data)
#                 response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#                 response['Content-Disposition'] = 'attachment; filename=Statisticreportallempl.docx'
#                 doc.save(response)
#                 return response
#
#             elif reportkind == 3:
#                 doc = DocxTemplate(os.path.join(BASE_DIR,"doc_templates/staticreport/statisticreportallsubdivisons.docx"))
#                 subdivisionlist = Subdivision.objects.all()
#                 data = {"list": [], "header": "Статистический отчет по кафедрам" + " за " + request.POST['reportingNIDyear'] + " год"}
#                 counter = 1
#                 for subdivision in subdivisionlist:
#                     makecounteryear(data, subdivision, counter, request.POST['reportingNIDyear'], request.POST['reportingNIDyear'])
#                     counter += 1
#                 doc.render(data)
#                 response = HttpResponse(
#                     content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#                 response['Content-Disposition'] = 'attachment; filename=Statisticreportallsubd.docx'
#                 doc.save(response)
#                 return response
#
#             elif reportkind == 4:
#                 doc = DocxTemplate("doc_templates/staticreport/statisticreportallsubdivisons_empl.docx")
#                 subdivisionlist = Subdivision.objects.all()
#                 data = {"list": [], "header": "Статистический отчет по кафедрам (с авторами)" + " за " + request.POST[
#                     'reportingNIDyear'] + " год"}
#                 counter = 1
#                 for subdivision in subdivisionlist:
#                     makecounteryearsubdiv_empl(data, subdivision, counter, request.POST['reportingNIDyear'],
#                                                request.POST['reportingNIDyear'])
#                     counter += 1
#                 doc.render(data)
#                 response = HttpResponse(
#                     content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#                 response['Content-Disposition'] = 'attachment; filename=Statisticreportallsubd.docx'
#                 doc.save(response)
#                 return response
#
#             elif reportkind == 5:
#                 doc = DocxTemplate("doc_templates/staticreport/statisticreportallsubdivisons_empl.docx")
#                 subdivision = Subdivision.objects.get(pk=request.POST['department'])
#                 data = {"list": [], "header": "Статистический отчет по кафедре " + subdivision.subdivisionname +  "(с авторами)" + " за " + request.POST[
#                     'reportingNIDyear'] + " год"}
#                 counter = 1
#                 makecounteryearsubdiv_empl(data, subdivision, counter, request.POST['reportingNIDyear'], request.POST['reportingNIDyear'])
#                 doc.render(data)
#                 response = HttpResponse(
#                     content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#                 response['Content-Disposition'] = 'attachment; filename=Statisticreportallsubd.docx'
#                 doc.save(response)
#                 return response
#
#
#         elif int(request.POST['yearradio']) == 2:
#             if reportkind == 0:
#                 doc = DocxTemplate("doc_templates/staticreport/statisticreportallemployees.docx")
#                 counter = 1
#                 author = Author.objects.get(pk=request.POST['authoridhidden1'])
#                 data = {"list": [],
#                         "header": "Статистический отчет по автору " + author.lastname + " " + author.firstname + " " + author.patronymic + " за " +
#                                   request.POST['reportingNIDyearsince'] + " - " + request.POST['reportingNIDyeartill'] + " годы"}
#                 makecounteryear(data, author, counter, request.POST['reportingNIDyearsince'], request.POST['reportingNIDyeartill'])
#                 doc.render(data)
#                 response = HttpResponse(
#                     content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#                 response['Content-Disposition'] = 'attachment; filename=Statisticreportallempl.docx'
#                 doc.save(response)
#                 return response
#
#             elif reportkind == 1:
#                 doc = DocxTemplate("doc_templates/staticreport/statisticreportallemployees.docx")
#                 counter = 1
#                 subdivision = Subdivision.objects.get(pk=request.POST['department'])
#                 data = {"list": [],
#                         "header": "Статистический отчет по " + subdivision.subdivisionname + " за " +
#                                   request.POST['reportingNIDyearsince'] + " - " + request.POST['reportingNIDyeartill'] + " годы"}
#                 makecounteryear(data, subdivision, counter, request.POST['reportingNIDyearsince'], request.POST['reportingNIDyeartill'])
#                 doc.render(data)
#                 response = HttpResponse(
#                     content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#                 response['Content-Disposition'] = 'attachment; filename=Statisticreportallempl.docx'
#                 doc.save(response)
#                 return response
#
#             elif reportkind == 2:
#                 doc = DocxTemplate("doc_templates/staticreport/statisticreportallemployees.docx")
#                 authorlist = Author.objects.all()
#                 data = {"list": [], "header": "Статистический отчет по сотрудникам за " +
#                                               request.POST['reportingNIDyearsince'] + " - " + request.POST['reportingNIDyeartill'] + " годы"}
#                 counter = 1
#                 for author in authorlist:
#                     makecounteryear(data, author, counter, request.POST['reportingNIDyearsince'], request.POST['reportingNIDyeartill'])
#                     counter+=1
#                 doc.render(data)
#                 response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#                 response['Content-Disposition'] = 'attachment; filename=Statisticreportallempl.docx'
#                 doc.save(response)
#                 return response
#
#             elif reportkind == 3:
#                 doc = DocxTemplate("doc_templates/staticreport/statisticreportallsubdivisons.docx")
#                 subdivisionlist = Subdivision.objects.all()
#                 data = {"list": [], "header": "Статистический отчет по кафедрам за " +
#                                               request.POST['reportingNIDyearsince'] + " - " + request.POST['reportingNIDyeartill'] + " годы"}
#                 counter = 1
#                 for subdivision in subdivisionlist:
#                     makecounteryear(data, subdivision, counter, request.POST['reportingNIDyearsince'], request.POST['reportingNIDyeartill'])
#                     counter += 1
#                 doc.render(data)
#                 response = HttpResponse(
#                     content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#                 response['Content-Disposition'] = 'attachment; filename=Statisticreportallsubd.docx'
#                 doc.save(response)
#                 return response
#
#             elif reportkind == 4:
#                 doc = DocxTemplate("doc_templates/staticreport/statisticreportallsubdivisons_empl.docx")
#                 subdivisionlist = Subdivision.objects.all()
#                 data = {"list": [], "header": "Статистический отчет по кафедрам (с авторами) за " +
#                                               request.POST['reportingNIDyearsince'] + " - " + request.POST['reportingNIDyeartill'] + " годы"}
#                 counter = 1
#                 for subdivision in subdivisionlist:
#                     makecounteryearsubdiv_empl(data, subdivision, counter, request.POST['reportingNIDyearsince'], request.POST['reportingNIDyeartill'])
#                     counter += 1
#                 doc.render(data)
#                 response = HttpResponse(
#                     content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#                 response['Content-Disposition'] = 'attachment; filename=Statisticreportallsubd.docx'
#                 doc.save(response)
#                 return response
#
#             elif reportkind == 5:
#                 doc = DocxTemplate("doc_templates/staticreport/statisticreportallsubdivisons_empl.docx")
#                 subdivision = Subdivision.objects.get(pk=request.POST['department'])
#                 data = {"list": [], "header": "Статистический отчет по кафедре " + subdivision.subdivisionname + "(с авторами) за " +
#                                               request.POST['reportingNIDyearsince'] + " - " + request.POST['reportingNIDyeartill'] + " годы"}
#                 counter = 1
#                 makecounteryearsubdiv_empl(data, subdivision, counter, request.POST['reportingNIDyearsince'], request.POST['reportingNIDyeartill'])
#                 doc.render(data)
#                 response = HttpResponse(
#                     content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#                 response['Content-Disposition'] = 'attachment; filename=Statisticreportallsubd.docx'
#                 doc.save(response)
#                 return response
#
#
# def publication(request):
#     monographlist = Publication.objects.filter(kind=Publicationkind.objects.get(pk=1)) # монографии
#     textbooklist = Publication.objects.filter(kind=Publicationkind.objects.get(pk=2)) # учебник
#     tutoriallist = Publication.objects.filter(kind=Publicationkind.objects.get(pk=3)) # учебное пособие
#     teachinglist = Publication.objects.filter(kind=Publicationkind.objects.get(pk=4)) # учебно-методическое пособие
#     practicallist = Publication.objects.filter(kind=Publicationkind.objects.get(pk=5)) # практическое пособиле
#     methodicaldevelopmentlist = Publication.objects.filter(kind=Publicationkind.objects.get(pk=6)) # методическая разработка
#     referenceeditionlist = Publication.objects.filter(kind=Publicationkind.objects.get(pk=7)) # справочное издание
#     commentarylist = Publication.objects.filter(kind=Publicationkind.objects.get(pk=8)) # комментарий законодательства
#     researcharticlelist = Publication.objects.filter(kind=Publicationkind.objects.get(pk=9)) # научная статья
#     conferencelist = Publication.objects.filter(kind=Publicationkind.objects.get(pk=10)) # материалы конференции
#     theseslist = Publication.objects.filter(kind=Publicationkind.objects.get(pk=11)) # тезисы докладов
#     otherlist = Publication.objects.filter(kind=Publicationkind.objects.get(pk=12)) # иная публикация
#
#     return render(request, 'reporting/puplicationreport.html', {'monographlist': monographlist,
#                                                                 'textbooklist': textbooklist,
#                                                                 'tutoriallist': tutoriallist,
#                                                                 'teachinglist': teachinglist,
#                                                                 'practicallist': practicallist,
#                                                                 'methodicaldevelopmentlist': methodicaldevelopmentlist,
#                                                                 'referenceeditionlist': referenceeditionlist,
#                                                                 'commentarylist': commentarylist,
#                                                                 'researcharticlelist': researcharticlelist,
#                                                                 'conferencelist': conferencelist,
#                                                                 'theseslist': theseslist,
#                                                                 'otherlist': otherlist})
#
#
#
# def ratingprofessor(request):
#
#     return render(request, 'reporting/ratingprofessor.html')
#
# def ratingsubdivision(request):
#
#     return render(request, 'reporting/ratingsubdivisions.html')

# def effectivenesnid(request):

# монография

# monographlist = Publication.objects.filter(kind__id=1)
# monographcountI = monographlist.filter(halfyear=1).count()
# monographcountII = monographlist.filter(halfyear=2).count()
# monographsheetcountI = 0
# monographsheetcountII = 0
# monographcountyear = monographlist.count()
#
# for monograph in monographlist:
#     if int(monograph.halfyear) == 1:
#         monographsheetcountI = monographsheetcountI + int(monograph.sheetcount)
#     elif int(monograph.halfyear) == 2:
#         monographsheetcountII = monographsheetcountII + int(monograph.sheetcount)
# monographsheetcountyear = monographsheetcountI + monographsheetcountII
#
# # учебник
#
# textbooklist = Publication.objects.filter(kind__id=2)
# textbookcountI = textbooklist.filter(halfyear=1).count()
# textbookcountII = textbooklist.filter(halfyear=2).count()
# textbooksheetcountI = 0
# textbooksheetcountII = 0
# textbookcountyear = textbooklist.count()
#
# for textbook in textbooklist:
#     if int(textbook.halfyear) == 1:
#         textbooksheetcountI = textbooksheetcountI + int(textbook.sheetcount)
#     elif int(textbook.halfyear) == 2:
#         textbooksheetcountII = textbooksheetcountII + int(textbook.sheetcount)
# textbooksheetcountyear = textbooksheetcountI + textbooksheetcountII

# return render(request, 'reporting/effectivenessNID.html')
# return render(request, 'reporting/effectivenessNID.html', {'monographcountI':monographcountI,
#                                                            'monographcountII': monographcountII,
#                                                            'monographsheetcountI': monographsheetcountI,
#                                                            'monographsheetcountII': monographsheetcountII,
#                                                            'monographcountyear': monographcountyear,
#                                                            'monographsheetcountyear': monographsheetcountyear,
#
#                                                            'textbookcountI': textbookcountI,
#                                                            'textbookcountII': textbookcountII,
#                                                            'textbooksheetcountI': textbooksheetcountI,
#                                                            'textbooksheetcountII': textbooksheetcountII,
#                                                            'textbookcountyear': textbookcountyear,
#                                                            'textbooksheetcountyear': textbooksheetcountyear
#
#
#
#
#
#
#
#
#                                                            })

#
# def magazines(request):
#     return render(request, 'reporting/magazines.html')
#
#
# def scienceevents(request):
#     return render(request, 'reporting/scientificevents.html')
#
#
# def pldreport(request):
#     pldlist = PLD.objects.all()
#     return render(request, 'reporting/pld.html', {'pldlist':pldlist})
#
#
# def anrreport(request):
#     return render(request, 'reporting/anrreport.html')
#
#
# def nirreport(request):
#     nirlist = NIR.objects.all()
#     return render(request, 'reporting/nirreport.html', {'nirlist':nirlist})
#
#
# def otherkindreport(request):
#     return render(request, 'reporting/otherreport.html')