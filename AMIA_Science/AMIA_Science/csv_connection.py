#exec(open('AMIA_SCIENCE/csv_connection.py').read())
from adaptor.fields import CharField,IntegerField#, IntegerField, DecimalField, DateField
from adaptor.model import CsvModel
import os
from AMIA_Science.settings import BASE_DIR
from sciencework.models import Publication,Author,AuthorsInPublication
from django.apps import apps
class AuthorsInPublicationCsvModel(CsvModel):
    publication = IntegerField()
    author = IntegerField()
    department = IntegerField()
    isauthor = IntegerField(default=0, null=True)
    code = IntegerField()
    class Meta:
        delimiter = ";"
        has_header = True
def find_db_value(csv_attr, model_attr, model_str, app,authors_in_publication_csv,authors_in_publication):
    Model = apps.get_model(app, model_str)
    if csv_attr is None or csv_attr == 0 :
        print ("Author In Publication {} has empty {}".format(authors_in_publication_csv.code,Model))
    instance_from_model = Model.objects.filter(id_access=getattr(authors_in_publication_csv,csv_attr))
    if len(instance_from_model) == 1:
        setattr(authors_in_publication, model_attr, instance_from_model[0])
    else:
        print ("Author In Publication {} has wrong {}".format(authors_in_publication_csv.code,Model))
authors_in_publication_list = AuthorsInPublicationCsvModel.import_data(data = open(os.path.join(os.path.dirname(BASE_DIR),"AMIA_Science/AMIA_Science/PublicationConnection.csv"),encoding='utf-8'))
def access_boolean(csv_attr,authors_in_publication_csv):
    if getattr(authors_in_publication_csv,csv_attr) == 0:
        return False
    elif getattr(authors_in_publication_csv,csv_attr) == 1:
        return True
    else:
        print ("Author In Publication {} has wrong {}".format(authors_in_publication_csv.code,csv_attr))
for authors_in_publication_csv in authors_in_publication_list:
    print (str(authors_in_publication_csv.code) + "- " + str(authors_in_publication_csv.publication) + " - " + str(authors_in_publication_csv.author))
    if authors_in_publication_csv.code == "" or authors_in_publication_csv.code is None:
        print ("Code is empty. why? " + authors_in_publication_csv.publication)  
    authors_in_publication_from_model = AuthorsInPublication.objects.filter(id_access=authors_in_publication_csv.code)
    if len(authors_in_publication_from_model) == 1:
        print ("Author In Publication {} exists".format(authors_in_publication_csv.code))
    elif len(authors_in_publication_from_model) ==0:
        print ("Author In Publication {} doesn't exist".format(authors_in_publication_csv.code))
        authors_in_publication = AuthorsInPublication.objects.create()
        authors_in_publication.id_access = authors_in_publication_csv.code
        find_db_value("publication","publication","Publication",'sciencework',authors_in_publication_csv,authors_in_publication)
        find_db_value("author","author","Author",'authors',authors_in_publication_csv,authors_in_publication)
        authors_in_publication.isauthor = access_boolean("isauthor",authors_in_publication_csv)
        authors_in_publication.save()
        #publication.outputdata = publication_csv.outputdata
        #publication.year = publication_csv.year
        #if publication_csv.halfyear > 0:
        #    publication.halfyear = publication_csv.halfyear
        #find_db_value("kind","kind","Publicationkind",publication_csv,publication)
        #publication.save()