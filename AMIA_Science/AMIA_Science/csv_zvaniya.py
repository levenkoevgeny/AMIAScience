#exec(open('AMIA_SCIENCE/csv_zvaniya.py').read())
from adaptor.fields import CharField,IntegerField
from adaptor.model import CsvModel
import os
from AMIA_Science.settings import BASE_DIR
from authors.models import Rank
class RankCsvModel(CsvModel):
    code = IntegerField()
    title = CharField()
    class Meta:
        delimiter = ";"
        has_header = True
rank_list = RankCsvModel.import_data(data = open(os.path.join(os.path.dirname(BASE_DIR),"AMIA_Science/AMIA_Science/Zvaniya.csv"),encoding='utf-8'))
for rank_csv in rank_list:
    print (str(rank_csv.code) + " " + rank_csv.title)
    rank_from_model = Rank.objects.filter(rank=rank_csv.title)
    if rank_csv.title is None or rank_csv.title == "":
        print ("Rank is empty. why? " + rank_csv.code)
    if len(rank_from_model) == 1:
        print ("Rank {} exists".format(rank_csv.title))
        #rank_from_model[0].id_access = rank_csv.code
        #rank_from_model[0].save()
    elif len(rank_from_model) ==0:
        rank = Rank.objects.create()
        rank.rank = rank_csv.title
        rank.id_access = rank_csv.code
        rank.save()
        print ("Rank {} created".format(rank.rank))