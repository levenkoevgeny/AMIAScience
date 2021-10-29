#exec(open('AMIA_SCIENCE/csv_publication.py').read())
from adaptor.fields import CharField,IntegerField
from adaptor.model import CsvModel
import os
from AMIA_Science.settings import BASE_DIR
from sciencework.models import Publication,Publicationkind,Subspecies
from django.apps import apps

class PublicationCsvModel(CsvModel):
    kind = IntegerField()
    outputdata = CharField()
    year = IntegerField()
    unused1 = CharField()
    unused2 = CharField()
    code = IntegerField()
    halfyear = IntegerField(default=0,null=True)
    class Meta:
        delimiter = ";"
        has_header = True
def find_db_value(csv_attr, model_attr, model_str, publication_csv,publication):
    Model = apps.get_model('sciencework', model_str)
    if csv_attr is None or csv_attr == 0 :
        print ("Publication {}. {} has empty {}".format(publication_csv.code,publication_csv.outputdata,Model))
    instance_from_model = Model.objects.filter(id_access=getattr(publication_csv,csv_attr))
    if len(instance_from_model) == 1:
        setattr(publication, model_attr, instance_from_model[0])
    else:
        print ("Publication {}. {} has wrong {}".format(publication_csv.code,publication_csv.outputdata,Model))
publication_list = PublicationCsvModel.import_data(data = open(os.path.join(os.path.dirname(BASE_DIR),"AMIA_Science/AMIA_Science/Publications_16.csv"),encoding='utf-8'))
for publication_csv in publication_list:
    print (str(publication_csv.code) + publication_csv.outputdata)
    if publication_csv.code == "" or publication_csv.code is None:
        print ("Code is empty. why? " + publication_csv.title)  
    publication_from_model = Publication.objects.filter(id_access=publication_csv.code)
    if len(publication_from_model) == 1:
        print ("Publication {}. {} exists. Updating outputdata and kind".format(publication_csv.code,publication_csv.outputdata))
        publication_from_model[0].outputdata = publication_csv.outputdata
        find_db_value("kind","kind","Publicationkind",publication_csv,publication_from_model[0])
        publication_from_model[0].save()
    elif len(publication_from_model) ==0:
        print ("Publication {}. {} doesn't exist".format(publication_csv.code,publication_csv.outputdata))
        publication = Publication.objects.create()
        publication.id_access = publication_csv.code
        publication.outputdata = publication_csv.outputdata
        publication.year = publication_csv.year
        if publication_csv.halfyear > 0:
            publication.halfyear = publication_csv.halfyear
        find_db_value("kind","kind","Publicationkind",publication_csv,publication)
        #publication.subspecies = Subspecies.objects.get(pk=6)
        publication.save()