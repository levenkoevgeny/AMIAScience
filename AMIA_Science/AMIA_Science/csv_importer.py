#exec(open('AMIA_SCIENCE/csv_importer.py').read())
from adaptor.fields import CharField,IntegerField,DateField,BooleanField#, , DecimalField, DateField
from adaptor.model import CsvModel
import os
from AMIA_Science.settings import BASE_DIR
from authors.models import Author,Subdivision,Position,Rank,Workstatus
from django.apps import apps
import datetime

class AuthorCsvModel(CsvModel):
    code = CharField()
    surname = CharField()
    name = CharField()
    patronymic = CharField()
    birth_date = DateField (**{'format':'%d.%m.%Y 0:00:00'},default=0, null=True) 
    podrazdelenie = IntegerField()
    dolznost = IntegerField(default=0, null=True)
    #dolznost2 = CharField()
    date_dolznost = DateField (**{'format':'%d.%m.%Y 0:00:00'},default=0, null=True)
    zvanie = IntegerField(default=0, null=True)
    iscandidate = IntegerField(default=0, null=True)
    candidatetitle = CharField()
    candidatedate = DateField (**{'format':'%d.%m.%Y 0:00:00'},default=0, null=True)
    isdoctor = IntegerField(default=0, null=True)
    doctortitle = CharField()
    doctordate = DateField (**{'format':'%d.%m.%Y 0:00:00'},default=0, null=True)
    isdocentvak = IntegerField(default=0, null=True)
    docentvakdate = DateField (**{'format':'%d.%m.%Y 0:00:00'},default=0, null=True)
    isprofessor = IntegerField(default=0, null=True)
    professordate = DateField (**{'format':'%d.%m.%Y 0:00:00'},default=0, null=True)
    isfired = IntegerField(default=0, null=True)
    extradata = CharField()

    class Meta:
        delimiter = ";"
        has_header = True
def find_db_value(csv_attr, model_attr, model_str, author_csv,author):
    Model = apps.get_model('authors', model_str)
    if csv_attr is None or csv_attr == 0 :
        print ("Author {}. {}{}{} has empty {}".format(author_csv.code,author_csv.surname,author_csv.name,author_csv.patronymic,Model))
    instance_from_model = Model.objects.filter(id_access=getattr(author_csv,csv_attr))
    if len(instance_from_model) == 1:
        setattr(author, model_attr, instance_from_model[0])
    else:
        print ("Author {}. {}{}{} has wrong {}".format(author_csv.code,author_csv.surname,author_csv.name,author_csv.patronymic,Model))
def access_boolean(csv_attr,author_csv):
    if getattr(author_csv,csv_attr) == 0:
        return False
    elif getattr(author_csv,csv_attr) == 1:
        return True
    else:
        print ("Author {}. {}{}{} has wrong {}".format(author_csv.code,author_csv.surname,author_csv.name,author_csv.patronymic,csv_attr))
def assign_value(csv_attr, model_attr, required_type,author_csv,author):
    #import pdb;pdb.set_trace()
    if type(getattr(author_csv,csv_attr)) == required_type:
        setattr(author, model_attr, getattr(author_csv,csv_attr))

author_list = AuthorCsvModel.import_data(data = open(os.path.join(os.path.dirname(BASE_DIR),"AMIA_Science/AMIA_Science/People.csv"),encoding='utf-8'))
for author_csv in author_list:
    print (author_csv.surname + author_csv.name + str(author_csv.birth_date) + str(author_csv.dolznost))
    if author_csv.code == "" or author_csv.code is None:
        print ("Code is empty. why? " + author_csv.surname)  
    author_from_model = Author.objects.filter(id_access=author_csv.code)
    if len(author_from_model) == 1:
        print ("Author {}. {}{}{} exists".format(author_csv.code,author_csv.surname,author_csv.name,author_csv.patronymic))
    elif len(author_from_model) ==0:
        author_csv.surname = author_csv.surname.replace(" ", "")
        author_csv.name = author_csv.name.replace(" ", "")
        author_csv.patronymic = author_csv.patronymic.replace(" ", "")
        print ("Author {}. {}{}{} doesn't exist".format(author_csv.code,author_csv.surname,author_csv.name,author_csv.patronymic))
        #import pdb;pdb.set_trace()
        author = Author.objects.create()
        author.id_access = author_csv.code
        find_db_value("podrazdelenie","subdivision","Subdivision",author_csv,author)
        author.lastname = author_csv.surname
        author.firstname = author_csv.name
        author.patronymic = author_csv.patronymic
        assign_value("birth_date","dateofbirth",datetime.datetime,author_csv,author)
        find_db_value("zvanie","rank","Rank",author_csv,author)
        find_db_value("dolznost","position","Position",author_csv,author)
        assign_value("date_dolznost","positiondate",datetime.datetime,author_csv,author)
        author.iscandidate = access_boolean("iscandidate",author_csv)
        author.candidatetitle = author_csv.candidatetitle
        assign_value("candidatedate","candidatedate",datetime.datetime,author_csv,author)
        author.isdoctor = access_boolean("isdoctor",author_csv)
        author.doctortitle = author_csv.doctortitle
        assign_value("doctordate","doctordate",datetime.datetime,author_csv,author)
        author.isdocentvak = access_boolean("isdocentvak",author_csv)
        assign_value("docentvakdate","docentvakdate",datetime.datetime,author_csv,author)
        author.isprofessor = access_boolean("isprofessor",author_csv)
        assign_value("professordate","professordate",datetime.datetime,author_csv,author)
        #import pdb;pdb.set_trace()
        if author_csv.isfired == 1:
            workstatus_from_model = Workstatus.objects.filter(id=2)
            if len(workstatus_from_model) == 1:
                author.workstatus = workstatus_from_model[0]
            else:
                print ("Workstatus 1 is wrong")
        elif author_csv.isfired == 0:
            workstatus_from_model = Workstatus.objects.filter(id=1)
            if len(workstatus_from_model) == 1:
                author.workstatus = workstatus_from_model[0]
            else:
                print ("Workstatus 0 is wrong")
        author.extradata = author_csv.extradata
        #import pdb;pdb.set_trace()
        '''subdivision_from_model = Subdivision.objects.filter(id_access=author_csv.podrazdelenie)
        if len(subdivision_from_model) == 1:
            author.subdivision = subdivision_from_model[0]
        else:
            print ("Author {}. {}{}{} has wrong subdivision {}".format(author_csv.code,author_csv.surname,author_csv.name,author_csv.patronymic,author_csv.podrazdelenie))
        #Проверять на 0
        position_from_model = Position.objects.filter(id_access=author_csv.dolznost)
        if len(position_from_model) == 1:
            author.position = position_from_model[0]
        elif len(position_from_model) ==0:
            print ("Author {}. {}{}{} has wrong position {}".format(author_csv.code,author_csv.surname,author_csv.name,author_csv.patronymic,author_csv.dolznost))
        '''
        '''rank_from_model = Rank.objects.filter(id_access=author_csv.zvanie)
        if len(rank_from_model) == 1:
            author.rank = rank_from_model[0]
        elif len(rank_from_model) ==0:
            print ("Author {}. {}{}{} has wrong rank {}".format(author_csv.code,author_csv.surname,author_csv.name,author_csv.patronymic,author_csv.zvanie))
'''


        author.save()
