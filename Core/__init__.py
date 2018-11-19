import pandas as pd
from django.conf import settings
import json
import os

table = pd.read_csv(os.path.join(settings.BASE_DIR, "data/main_table.csv"), sep=';')
addresses = pd.read_csv(os.path.join(settings.BASE_DIR, "data/addresses.csv"), sep=';')


def _find_schools(name):
    return table['name'].str.contains(name, regex=False)


def simple_search(name):
    # TODO: remove redundant columns
    return table[_find_schools(name)]


def adv_search(**params):
    # TODO
    return []


def get_school_json(ekis_id):
    return json.dumps(get_school(ekis_id))


def get_school(ekis_id):
    t = table[table.ekis_id == ekis_id]
    '''name
        name_full
        site
        email
        phone
        principal
        stud_from
        stud_to
        prophiles
        address
        ogrn
        okato
        financing
        ou_type
        ou_class
        ege_mean
        subjects_ege - dict "name": "balls"
        subjects_oge - как subjects_ege
        
        address: filltext; isMain
        schools_like_this: (ekis, name) or {"ekis": "name"}
        '''
    if len(t) != 1:
        return {}
    res = {
        "name": str(t.name[0]),
        "name_full": str(t.name_full[0]),
        "site": str(t.site[0]),
        "email": str(t.email[0]),
        "phone": str(t.phone[0]),
        "principal": str(t.principal[0]),
        "stud_from": t.stud_from[0],
        "stud_to": str(t.stud_to[0]),
        "prophiles": str(t.prophiles[0]),
        "address": str(t.address[0]),
        "ogrn": str(t.ogrn[0]),
        "okato": str(t.okato[0]),
        "financing": str(t.financing[0]),
        "ou_type": str(t.ou_type[0]),
        "ou_class": str(t.ou_class[0]),
        "ege_mean": t.ege_mean[0],
        "subjects_ege": {},
        "subjects_oge": {},
        "addresses": [],
        "schools_like_this": [t.schools_like_this1, t.schools_like_this2, t.schools_like_this3, t.schools_like_this4,
                              t.schools_like_this5, t.schools_like_this6, t.schools_like_this7, t.schools_like_this8,
                              t.schools_like_this9, t.schools_like_this10]
    }
    ege = 'Русский язык\nМатематика профильная\nОбществознание\nАнглийский язык\nФизика\nИстория\nБиология' \
          'Информатика и ИКТ\nХимия\nЛитература\nГеография\nФранцузcкий язык\nНемецкий язык\nИспанский язык'.split('\n')
    oge = 'Математика\nРусский язык\nОбществознание\nАнглийский язык\nИнформатика\nБиология\nГеография\nФизика\nХимия' \
          '\nИстория\nЛитература\nФранцузский язык\nНемецкий язык\nИспанский язык'.split('\n')
    for subj in ege:
        res['subjects_ege'][subj] = res["ЕГЭ_" + subj][0]
    for subj in oge:
        res['subjects_oge'][subj] = res["ОГЭ_" + subj][0]

    for building in addresses[addresses.ekis_id == ekis_id]:
        res['addresses'].append({'isMain': building.isMain, 'fulltext': building.fulltext})
    return res


def get_school_name(ekis):
    return table[table.ekis == ekis].name[0]


def get_schools_short(ekisis):
    t = []
    ekisis = set(ekisis)
    for ind in range(len(table)):
        if table[ind].ekis_id in ekisis:
            t.append(table[ind])
        pass
    return json.dumps(t)
