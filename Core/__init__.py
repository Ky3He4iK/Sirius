import pandas as pd
from django.conf import settings
import json
import os

table = pd.read_csv(os.path.join(settings.BASE_DIR, "data/main_table.csv"), sep=';')
addresses = pd.read_csv(os.path.join(settings.BASE_DIR, "data/addresses.csv"), sep=';')


def _find_schools(name):
    return table['name'].str.contains(name, regex=False)


def _get_school_pair(ekis):
    return ekis, table[table.ekis_id == ekis].name[0]


def _get_school_short(ekis_id):
    t = table[table.ekis_id == ekis_id]
    '''name
        profiles
        address
        ou_class
        '''
    if len(t) != 1:
        return {}
    res = {
        "name": str(t.name[0]),
        "profiles": [],
        "address": str(t.address[0]),
        "ou_class": str(t.ou_class[0]),
        "addresses": []
    }
    profiles = 'Языковой\nЕстественнонаучный\nТехнический\nГуманитарный\nЭкономический'.split('\n')
    for prophile in profiles:
        if t["П_" + prophile][0] == 1:
            res['profiles'].append(prophile)

    tt = addresses[addresses.ekis_id == ekis_id]
    for ind in range(len(tt)):
        res['addresses'].append({'isMain': tt['isMain'][ind], 'fulltext': tt['fulltext'][ind],
                                 'latLng': [tt['lat'][ind], tt['lng'][ind]]})
    return res


def _get_school_short_ind(ind):
    '''name
        profiles
        address
        ou_class
        addresses
    '''
    res = {
        "name": str(table.name[ind]),
        "profiles": [],
        "address": str(table.address[ind]),
        "ou_class": str(table.ou_class[ind]),
        "addresses": []
    }
    profiles = 'Языковой\nЕстественнонаучный\nТехнический\nГуманитарный\nЭкономический'.split('\n')
    for prophile in profiles:
        if table["П_" + prophile][ind] == 1:
            res['profiles'].append(prophile)
    tt = addresses[addresses.ekis_id == table.ekis_id[ind]]
    for ind in range(len(tt)):
        res['addresses'].append({'isMain': tt['isMain'][ind], 'fulltext': tt['fulltext'][ind],
                                 'latLng': [tt['lat'][ind], tt['lng'][ind]]})
    return res


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
        profiles
        address
        ogrn
        okato
        ou_type
        ou_class
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
        "stud_to": t.stud_to[0],
        "profiles": [],
        "address": str(t.address[0]),
        "ogrn": str(t.ogrn[0]),
        "okato": str(t.okato[0]),
        "ou_type": str(t.ou_type[0]),
        "ou_class": str(t.ou_class[0]),
        "subjects_ege": {},
        "subjects_oge": {},
        "addresses": [],
        "schools_like_this": [
            _get_school_pair(t.schools_like_this1[0]),
            _get_school_pair(t.schools_like_this2[0]),
            _get_school_pair(t.schools_like_this3[0]),
            _get_school_pair(t.schools_like_this4[0]),
            _get_school_pair(t.schools_like_this5[0]),
            _get_school_pair(t.schools_like_this6[0]),
            _get_school_pair(t.schools_like_this7[0]),
            _get_school_pair(t.schools_like_this8[0]),
            _get_school_pair(t.schools_like_this9[0]),
            _get_school_pair(t.schools_like_this10[0]),
        ]
    }
    ege = 'Русский язык\nМатематика профильная\nОбществознание\nАнглийский язык\nФизика\nИстория\nБиология' \
          'Информатика и ИКТ\nХимия\nЛитература\nГеография\nФранцузcкий язык\nНемецкий язык\nИспанский язык'.split('\n')
    oge = 'Математика\nРусский язык\nОбществознание\nАнглийский язык\nИнформатика\nБиология\nГеография\nФизика\nХимия' \
          '\nИстория\nЛитература\nФранцузский язык\nНемецкий язык\nИспанский язык'.split('\n')
    profiles = 'Языковой\nЕстественнонаучный\nТехнический\nГуманитарный\nЭкономический'.split('\n')
    for subj in ege:
        res['subjects_ege'][subj] = t["ЕГЭ_" + subj][0]
    for subj in oge:
        res['subjects_oge'][subj] = t["ОГЭ_" + subj][0]

    for prophile in profiles:
        if t["П_" + prophile][0] == 1:
            res['profiles'].append(prophile)
    tt = addresses[addresses.ekis_id == ekis_id]
    for ind in range(len(tt)):
        res['addresses'].append({'isMain': tt['isMain'][ind], 'fulltext': tt['fulltext'][ind],
                                 'latLng': [tt['lat'][ind], tt['lng'][ind]]})
    return res


def get_school_name(ekis):
    return table[table.ekis == ekis].name[0]


def get_schools_short(ekises):
    return [_get_school_short(ekis) for ekis in ekises]


def get_schools_by_string(string):
    res = []
    for i, name in enumerate(table.name):
        if string in name:
            res.append(_get_school_short_ind(i))
    return res


def get_schools_filter(filters):
    # TODO: do
    res = []
    '''
    
    '''
    return get_schools_short(res)


def get_schools_short_json(ekises):
    return json.dumps(get_schools_short(ekises))


def get_schools_by_string_json(string):
    return json.dumps(get_schools_by_string(string))


def get_schools_filter_json(filters):
    return json.dumps(get_schools_short(filters))
