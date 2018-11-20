import pandas as pd
from django.conf import settings
import json
import os

_table = pd.read_csv(os.path.join(settings.BASE_DIR, "data/main_table.csv"), sep=';')
_addresses = pd.read_csv(os.path.join(settings.BASE_DIR, "data/addresses.csv"), sep=';')
_coordinates = [{'ekis_id': _addresses.ekis_id[ind], 'fulltext': _addresses.fulltext[ind],
                'latLng': [_addresses.lat[ind], _addresses.lng[ind]]} for ind in range(len(_addresses))]
_profiles = [col[2:] for col in list(_table.columns) if col[:2] == "П_"]
_ege = [col[4:] for col in list(_table.columns) if col[:4] == "ЕГЭ_"]
_oge = [col[4:] for col in list(_table.columns) if col[:4] == "ОГЭ_"]


def _find_schools(name):
    return _table['name'].str.contains(name, regex=False)


def _get_school_pair(ekis):
    return ekis, _table[_table.ekis_id == ekis].name[0]


def _addresses_to_arr(tt):
    return [{'isMain': tt['isMain'][ind], 'fulltext': tt['fulltext'][ind],
             'latLng': [tt['lat'][ind], tt['lng'][ind]]} for ind in range(len(tt))]


def _profiles_to_arr(t, ind=0):
    return [profile for profile in _profiles if t["П_" + profile][ind] == 1]


def _get_school_short(ekis_id):
    t = _table[_table.ekis_id == ekis_id]
    '''name
        profiles
        address
        ou_class
        addresses
        '''
    if len(t) != 1:
        return {}
    res = {
        "name": str(t.name[0]),
        "profiles": _profiles_to_arr(t),
        "address": str(t.address[0]),
        "ou_class": str(t.ou_class[0]),
        "addresses": _addresses_to_arr(_addresses[_addresses.ekis_id == ekis_id]),
    }
    return res


def _get_school_short_ind(ind):
    '''name
        profiles
        address
        ou_class
        addresses
    '''
    res = {
        "name": str(_table.name[ind]),
        "profiles": _profiles_to_arr(_table, ind),
        "address": str(_table.address[ind]),
        "ou_class": str(_table.ou_class[ind]),
        "addresses": _addresses_to_arr(_addresses[_addresses.ekis_id == _table.ekis_id[ind]]),
    }
    return res


def _get_schools_short(ekises):
    return [_get_school_short(ekis) for ekis in ekises]


def get_school(ekis_id):
    t = _table[_table.ekis_id == ekis_id]
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
        "profiles": _profiles_to_arr(t),
        "address": str(t.address[0]),
        "ogrn": str(t.ogrn[0]),
        "okato": str(t.okato[0]),
        "ou_type": str(t.ou_type[0]),
        "ou_class": str(t.ou_class[0]),
        "subjects_ege": {subj: t["ЕГЭ_" + subj][0] for subj in _ege},
        "subjects_oge": {subj: t["ОГЭ_" + subj][0] for subj in _oge},
        "addresses": _addresses_to_arr(_addresses[_addresses.ekis_id == ekis_id]),
        "schools_like_this": [_get_school_pair(t['schools_like_this' + str(i)][0]) for i in range(1, 11)],
    }
    return res


def get_schools_by_string(string):
    res = []
    for i, name in enumerate(_table.name):
        if string in name:
            res.append(_get_school_short_ind(i))
    return res


def get_schools_filter(filters):
    # TODO: do
    res = []
    '''
    
    '''
    return _get_schools_short(res)


def get_school_json(ekis_id):
    return json.dumps(get_school(ekis_id))


def get_schools_by_string_json(string):
    return json.dumps(get_schools_by_string(string))


def get_schools_filter_json(filters):
    return json.dumps(get_schools_filter(filters))


def get_lists():
    return json.dumps({
        'coordinates': _coordinates,
        'profiles': _profiles,
        'ege': _ege,
        'oge': _oge
    })
