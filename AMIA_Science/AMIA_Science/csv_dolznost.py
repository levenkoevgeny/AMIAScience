#exec(open('AMIA_SCIENCE/csv_dolznost.py').read())
from adaptor.fields import CharField,IntegerField#, IntegerField, DecimalField, DateField
from adaptor.model import CsvModel
import os
from AMIA_Science.settings import BASE_DIR
from authors.models import Position
class DolznostCsvModel(CsvModel):
    code = IntegerField()
    dolznost = CharField()
    #Telefon_R = CharField()
    #Telefon_S = CharField()

    class Meta:
        delimiter = ";"
        has_header = True
dolznost_list = DolznostCsvModel.import_data(data = open(os.path.join(os.path.dirname(BASE_DIR),"AMIA_Science/AMIA_Science/Dolznost.csv"),encoding='utf-8'))
for dolznost_csv in dolznost_list:
    print (str(dolznost_csv.code) + " " + dolznost_csv.dolznost)
    dolznost_from_model = Position.objects.filter(positionname=dolznost_csv.dolznost)
    if dolznost_csv.dolznost == "" or dolznost_csv.dolznost is None:
        print ("Donznsot is empty. why? " + dolznost_csv.code)
    if len(dolznost_from_model) == 1:
        print ("Dolznost {} exists".format(dolznost_csv.dolznost))
    elif len(dolznost_from_model) ==0:
        dolznost = Position.objects.create()
        dolznost.positionname = dolznost_csv.dolznost
        dolznost.id_access = dolznost_csv.code
        dolznost.save()
        print ("Dolznost {} created".format(dolznost.positionname))
