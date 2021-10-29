#exec(open('AMIA_SCIENCE/csv_podrazdelenie.py').read())
from adaptor.fields import CharField,IntegerField#, IntegerField, DecimalField, DateField
from adaptor.model import CsvModel
import os
from AMIA_Science.settings import BASE_DIR
from authors.models import Subdivision,Subdivisiongroup
class PodrazdelenieCsvModel(CsvModel):
    code = IntegerField()
    title_short = CharField()
    title = CharField()
    #Telefon_R = CharField()
    #Telefon_S = CharField()

    class Meta:
        delimiter = ";"
        has_header = True
podrazdelenie_list = PodrazdelenieCsvModel.import_data(data = open(os.path.join(os.path.dirname(BASE_DIR),"AMIA_Science/AMIA_Science/Podrazdelenie.csv"),encoding='utf-8'))
for podrazdelenie_csv in podrazdelenie_list:
    print (str(podrazdelenie_csv.code) + " " + podrazdelenie_csv.title)
    podrazdelenie_from_model = Subdivision.objects.filter(subdivisionname=podrazdelenie_csv.title)
    if podrazdelenie_csv.title is None or podrazdelenie_csv.title == "":
        print ("Podrazdenenie is empty. why? " + dolznost_csv.code)
    if len(podrazdelenie_from_model) == 1:
        print ("Podrazdelenie {} exists".format(podrazdelenie_csv.title))
    elif len(podrazdelenie_from_model) ==0:
        podrazdelenie = Subdivision.objects.create()
        suddivision_group = Subdivisiongroup.objects.get(pk=1)
        podrazdelenie.subdivisionname = podrazdelenie_csv.title
        podrazdelenie.id_access = podrazdelenie_csv.code
        podrazdelenie.group = suddivision_group
        podrazdelenie.save()
        print ("Podrazdelenie {} created".format(podrazdelenie.subdivisionname))
