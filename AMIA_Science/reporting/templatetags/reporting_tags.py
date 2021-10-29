from django import template
from sciencework.models import Publication, Publicationkind
from anr.models import ANR
from otherkind.models import Otherkind

register = template.Library()


# ПО ГОДУ

# количество работ по году
@register.filter(name='sciencework_count_all')
def sciencework_count_all(value, args):
    return value.filter(year=args).count()


# количество работ по году - первое полугодие
@register.filter(name='sciencework_count_all_I')
def sciencework_count_all_I(value, args):
    return value.filter(year=args).filter(halfyear='1').count()


# количество работ по году - второе полугодие
@register.filter(name='sciencework_count_all_II')
def sciencework_count_all_II(value, args):
    return value.filter(year=args).filter(halfyear='2').count()


# количество страниц по году
@register.filter(name='sciencework_sheet_count_all_for_year')
def sciencework_sheet_count_all_for_year(value, args):
    counter_list = value.filter(year=args)
    sheetcount_sum = 0
    for s_w in counter_list:
        if s_w.sheetcount:
            sheetcount_sum = sheetcount_sum + float(s_w.sheetcount)
    return round(sheetcount_sum, 2)


# количество страниц по году - первое полугодие
@register.filter(name='sciencework_sheet_count_all_for_year_I')
def sciencework_sheet_count_all_for_year_I(value, args):
    counter_list = value.filter(year=args).filter(halfyear='1')
    sheetcount_sum = 0
    for s_w in counter_list:
        if s_w.sheetcount:
            sheetcount_sum = sheetcount_sum + float(s_w.sheetcount)
    return round(sheetcount_sum, 2)


# количество страниц по году - второе полугодие
@register.filter(name='sciencework_sheet_count_all_for_year_II')
def sciencework_sheet_count_all_for_year_II(value, args):
    counter_list = value.filter(year=args).filter(halfyear='2')
    sheetcount_sum = 0
    for s_w in counter_list:
        if s_w.sheetcount:
            sheetcount_sum = sheetcount_sum + float(s_w.sheetcount)
    return round(sheetcount_sum, 2)


# ПО ВИДУ И ГОДУ

@register.filter(name='sciencework_count_all_pages')
def sciencework_count_all_pages(value, args):
    counter_list = value.filter(kind_id=args)
    sheetcount_sum = 0
    for s_w in counter_list:
        if s_w.sheetcount:
            sheetcount_sum = sheetcount_sum + float(s_w.sheetcount)
    return round(sheetcount_sum, 2)


@register.filter(name='sciencework_count_all_pages_I')
def sciencework_count_all_pages_I(value, args):
    counter_list = value.filter(kind_id=args).filter(halfyear='1')
    sheetcount_sum = 0
    for s_w in counter_list:
        if s_w.sheetcount:
            sheetcount_sum = sheetcount_sum + float(s_w.sheetcount)
    return round(sheetcount_sum, 2)


@register.filter(name='sciencework_count_all_pages_II')
def sciencework_count_all_pages_II(value, args):
    counter_list = value.filter(kind_id=args).filter(halfyear='2')
    sheetcount_sum = 0
    for s_w in counter_list:
        if s_w.sheetcount:
            sheetcount_sum = sheetcount_sum + float(s_w.sheetcount)
    return round(sheetcount_sum, 2)


# ПО ВИДУ И ГОДУ

# количество работ по виду и году
@register.filter(name='sciencework_count')
def sciencework_count(value, args):
    arg_list = [arg.strip() for arg in args.split(',')]
    return value.filter(kind_id=arg_list[0]).filter(year=arg_list[1]).count()


# количество страниц по виду и году
@register.filter(name='sciencework_count_pages')
def sciencework_count_pages(value, args):
    arg_list = [arg.strip() for arg in args.split(',')]
    counter_list = value.filter(kind_id=arg_list[0]).filter(year=arg_list[1])
    sheetcount_sum = 0
    for s_w in counter_list:
        if s_w.sheetcount:
            sheetcount_sum = sheetcount_sum + float(s_w.sheetcount)
    return round(sheetcount_sum, 2)


# количество работ по виду и году - первое полугодие
@register.filter(name='sciencework_count_I')
def sciencework_count_I(value, args):
    arg_list = [arg.strip() for arg in args.split(',')]
    return value.filter(kind_id=arg_list[0]).filter(year=arg_list[1]).filter(halfyear='1').count()


# количество страниц по виду и году - первое полугодие
@register.filter(name='sciencework_count_I_pages')
def sciencework_count_I_pages(value, args):
    arg_list = [arg.strip() for arg in args.split(',')]
    counter_list = value.filter(kind_id=arg_list[0]).filter(year=arg_list[1]).filter(halfyear='1')
    sheetcount_sum = 0
    for s_w in counter_list:
        if s_w.sheetcount:
            sheetcount_sum = sheetcount_sum + float(s_w.sheetcount)
    return round(sheetcount_sum, 2)


# количество работ по виду и году - второе полугодие
@register.filter(name='sciencework_count_II')
def sciencework_count_II(value, args):
    arg_list = [arg.strip() for arg in args.split(',')]
    return value.filter(kind_id=arg_list[0]).filter(year=arg_list[1]).filter(halfyear='2').count()


# количество страниц по виду и году - второе полугодие
@register.filter(name='sciencework_count_II_pages')
def sciencework_count_II_pages(value, args):
    arg_list = [arg.strip() for arg in args.split(',')]
    counter_list = value.filter(kind_id=arg_list[0]).filter(year=arg_list[1]).filter(halfyear='2')
    sheetcount_sum = 0
    for s_w in counter_list:
        if s_w.sheetcount:
            sheetcount_sum = sheetcount_sum + float(s_w.sheetcount)
    return round(sheetcount_sum, 2)


@register.filter(name='sciencework_count_subspecies')
def sciencework_count_subspecies(value, args_subspecies):
    arg_list = [arg.strip() for arg in args_subspecies.split(',')]
    return value.filter(subspecies_id=arg_list[0]).filter(year=arg_list[1]).count()


@register.filter(name='sciencework_count_subspecies_I')
def sciencework_count_subspecies(value, args_subspecies):
    arg_list = [arg.strip() for arg in args_subspecies.split(',')]
    return value.filter(subspecies_id=arg_list[0]).filter(year=arg_list[1]).filter(halfyear='1').count()


@register.filter(name='sciencework_count_subspecies_II')
def sciencework_count_subspecies(value, args_subspecies):
    arg_list = [arg.strip() for arg in args_subspecies.split(',')]
    return value.filter(subspecies_id=arg_list[0]).filter(year=arg_list[1]).filter(halfyear='2').count()


@register.filter(name='sciencework_count_grif')
def sciencework_count_grif(value, args_grif):
    arg_list = [arg.strip() for arg in args_grif.split(',')]
    return value.filter(grif_id=arg_list[0]).filter(year=arg_list[1]).count()


@register.filter(name='sciencework_count_grif_I')
def sciencework_count_grif(value, args_grif):
    arg_list = [arg.strip() for arg in args_grif.split(',')]
    return value.filter(grif_id=arg_list[0]).filter(year=arg_list[1]).filter(halfyear='1').count()


@register.filter(name='sciencework_count_grif_II')
def sciencework_count_grif(value, args_grif):
    arg_list = [arg.strip() for arg in args_grif.split(',')]
    return value.filter(grif_id=arg_list[0]).filter(year=arg_list[1]).filter(halfyear='2').count()


@register.filter(name='sciencework_count_all_subspecies')
def sciencework_count_all_subspecies(value, args):
    return value.filter(subspecies_id=args).count()


@register.filter(name='sciencework_count_all_subspecies_I')
def sciencework_count_all_subspecies(value, args):
    return value.filter(subspecies_id=args).filter(halfyear='1').count()


@register.filter(name='sciencework_count_all_subspecies_II')
def sciencework_count_all_subspecies(value, args):
    return value.filter(subspecies_id=args).filter(halfyear='2').count()


@register.filter(name='sciencework_count_all_grif')
def sciencework_count_all_grif(value, args):
    return value.filter(grif_id=args).count()


@register.filter(name='sciencework_count_all_grif_I')
def sciencework_count_all_grif(value, args):
    return value.filter(grif_id=args).filter(halfyear='1').count()


@register.filter(name='sciencework_count_all_grif_II')
def sciencework_count_all_grif(value, args):
    return value.filter(grif_id=args).filter(halfyear='2').count()


@register.filter(name='sciencework_count_all_kind')
def sciencework_count_all_kind(value, args):
    return value.filter(kind_id=args).count()


@register.filter(name='sciencework_count_all_kind_I')
def sciencework_count_all_kind(value, args):
    return value.filter(kind_id=args).filter(halfyear='1').count()


@register.filter(name='sciencework_count_all_kind_II')
def sciencework_count_all_kind(value, args):
    return value.filter(kind_id=args).filter(halfyear='2').count()













@register.filter(name='sciencework_publication_all_invak')
def sciencework_publication_all_invak(value, args):
    return value.filter(kind_id=args).filter(invak=True).count()


@register.filter(name='all_is_forum_result')
def all_is_forum_result(value, args):
    return value.filter(kind_id=args).filter(invak=False).filter(is_forum_result=True).count()


@register.filter(name='sciencework_publication_all_invak_I')
def sciencework_publication_all_invak_I(value, args):
    return value.filter(kind_id=args).filter(invak=True).filter(halfyear='1').count()


@register.filter(name='all_is_forum_result_I')
def all_is_forum_result_I(value, args):
    return value.filter(kind_id=args).filter(invak=False).filter(is_forum_result=True).filter(halfyear='1').count()


@register.filter(name='sciencework_publication_all_invak_II')
def sciencework_publication_all_invak_II(value, args):
    return value.filter(kind_id=args).filter(invak=True).filter(halfyear='2').count()


@register.filter(name='all_is_forum_result_II')
def all_is_forum_result_II(value, args):
    return value.filter(kind_id=args).filter(invak=False).filter(is_forum_result=True).filter(halfyear='2').count()


@register.filter(name='sciencework_publication_all_not_invak')
def sciencework_publication_all_not_invak(value, args):
    return value.filter(kind_id=args).filter(invak=False).count()


@register.filter(name='sciencework_publication_all_not_invak_I')
def sciencework_publication_all_not_invak_I(value, args):
    return value.filter(kind_id=args).filter(invak=False).filter(halfyear='1').count()


@register.filter(name='sciencework_publication_all_not_invak_II')
def sciencework_publication_all_not_invak_II(value, args):
    return value.filter(kind_id=args).filter(invak=False).filter(halfyear='2').count()


@register.filter(name='sciencework_publication_invak')
def sciencework_publication_invak(value, args):
    arg_list = [arg.strip() for arg in args.split(',')]
    return value.filter(kind_id=arg_list[0]).filter(year=arg_list[1]).filter(invak=True).count()


@register.filter(name='is_forum_result')
def is_forum_result(value, args):
    arg_list = [arg.strip() for arg in args.split(',')]
    return value.filter(kind_id=arg_list[0]).filter(year=arg_list[1]).filter(invak=False).filter(is_forum_result=True).count()


@register.filter(name='sciencework_publication_invak_I')
def sciencework_publication_invak(value, args):
    arg_list = [arg.strip() for arg in args.split(',')]
    return value.filter(kind_id=arg_list[0]).filter(year=arg_list[1]).filter(invak=True).filter(halfyear='1').count()


@register.filter(name='is_forum_result_I')
def is_forum_result_I(value, args):
    arg_list = [arg.strip() for arg in args.split(',')]
    return value.filter(kind_id=arg_list[0]).filter(year=arg_list[1]).filter(invak=False).filter(is_forum_result=True).filter(halfyear='1').count()


@register.filter(name='is_forum_result_II')
def is_forum_result_II(value, args):
    arg_list = [arg.strip() for arg in args.split(',')]
    return value.filter(kind_id=arg_list[0]).filter(year=arg_list[1]).filter(invak=False).filter(is_forum_result=True).filter(halfyear='2').count()


@register.filter(name='sciencework_publication_invak_II')
def sciencework_publication_invak(value, args):
    arg_list = [arg.strip() for arg in args.split(',')]
    return value.filter(kind_id=arg_list[0]).filter(year=arg_list[1]).filter(invak=True).filter(halfyear='2').count()


@register.filter(name='sciencework_publication_not_invak')
def sciencework_publication_not_invak(value, args):
    arg_list = [arg.strip() for arg in args.split(',')]
    return value.filter(kind_id=arg_list[0]).filter(year=arg_list[1]).filter(invak=False).count()


@register.filter(name='sciencework_publication_not_invak_I')
def sciencework_publication_not_invak(value, args):
    arg_list = [arg.strip() for arg in args.split(',')]
    return value.filter(kind_id=arg_list[0]).filter(year=arg_list[1]).filter(invak=False).filter(halfyear='1').count()


@register.filter(name='sciencework_publication_not_invak_II')
def sciencework_publication_not_invak(value, args):
    arg_list = [arg.strip() for arg in args.split(',')]
    return value.filter(kind_id=arg_list[0]).filter(year=arg_list[1]).filter(invak=False).filter(halfyear='2').count()


@register.filter(name='anr_year')
def anr_year(value, args):
    return value.filter(other_year=args).count()


@register.filter(name='add_string')
def add_string(value, arg):
    return str(value) + ',' + str(arg)
