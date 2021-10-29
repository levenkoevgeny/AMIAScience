#exec(open('AMIA_SCIENCE/csv_publication_subdivision.py').read())
from adaptor.fields import CharField,IntegerField#, IntegerField, DecimalField, DateField
from adaptor.model import CsvModel
import os
from AMIA_Science.settings import BASE_DIR
from sciencework.models import Publication,Author,AuthorsInPublication,Subdivision
from django.apps import apps
class SubdivisionInPublicationCsvModel(CsvModel):
    publication = IntegerField()
    author = IntegerField()
    subdivision = IntegerField()
    isauthor = IntegerField(default=0, null=True)
    code = IntegerField()
    class Meta:
        delimiter = ";"
        has_header = True
        ##CUSTOMISED FUNCTION!
def find_db_value(csv_attr,  model_str, app,subdivision_in_publication_csv,subdivision_in_publication):
    Model = apps.get_model(app, model_str)
    if csv_attr is None or csv_attr == 0 :
        print ("Author In Publication {} has empty {}".format(subdivision_in_publication_csv.code,Model))
    instance_from_model = Model.objects.filter(id_access=getattr(subdivision_in_publication_csv,csv_attr))
    if len(instance_from_model) == 1:
    	subdivision_in_publication.subdivisions.add(instance_from_model[0])
        #setattr(subdivision_in_publication, model_attr, instance_from_model[0])
    else:
        print ("Subdivision In Publication {} has wrong {}".format(subdivision_in_publication_csv.code,Model))
subdivision_in_publication_list = SubdivisionInPublicationCsvModel.import_data(data = open(os.path.join(os.path.dirname(BASE_DIR),"AMIA_Science/AMIA_Science/PublicationConnection.csv"),encoding='utf-8'))
for subdivision_in_publication_csv in subdivision_in_publication_list:
    print (str(subdivision_in_publication_csv.code) + "- " + str(subdivision_in_publication_csv.subdivision) + " - " + str(subdivision_in_publication_csv.author))
    if subdivision_in_publication_csv.code == "" or subdivision_in_publication_csv.code is None:
        print ("Code is empty. why? " + subdivision_in_publication_csv.publication)  
    else:
    	publication_from_model = Publication.objects.filter(id_access=subdivision_in_publication_csv.publication)
    	if len(publication_from_model) == 1:
    		find_db_value("subdivision","Subdivision",'authors',subdivision_in_publication_csv,publication_from_model[0])
    		publication_from_model[0].save()
    	else:
    		print ("Publication {} has wrong id ".format(subdivision_in_publication_csv.publication))