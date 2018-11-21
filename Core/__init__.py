import pandas as pd
from django.conf import settings
import json
import os

_table = pd.read_csv(os.path.join(settings.BASE_DIR, "data/main_table.csv"), sep=';')
_addresses = pd.read_csv(os.path.join(settings.BASE_DIR, "data/addresses.csv"), sep=';')
_coordinates = [{'ekis_id': int(_addresses.ekis_id[ind]), 'fulltext': _addresses.fulltext[ind],
                'latLng': [_addresses.lat[ind], _addresses.lng[ind]]} for ind in range(len(_addresses))]
_profiles = [col[2:] for col in list(_table.columns) if col[:2] == "П_"]
_ege = [col[4:] for col in list(_table.columns) if col[:4] == "EGE_"]
_oge = [col[4:] for col in list(_table.columns) if col[:4] == "OGE_"]


def _find_schools(name):
    return _table['name'].str.contains(name, regex=False)


def _get_school_pair(ekis):
    return int(ekis), str(_table[_table.ekis_id == ekis].name[0])


def _addresses_to_arr(tt):
    return [{'isMain': bool(tt['isMain'][ind]), 'fulltext': tt['fulltext'][ind],
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


def _get_schools_short_ind(inds):
    return [_get_school_short_ind(ind) for ind in inds]


def _filtering(filters):
    def _filter_by_district(names):
        return [ind for (ind, district) in enumerate(_addresses.disctrict) if district in names]

    def _filter_by_class(number):
        return [ind for ind in inds if _table.stud_from[ind] <= number <= _table.stud_to[ind]]

    def _filter_by_profiles(profiles):
        sets = [set([ind for ind in inds if profile in _profiles and _table['П_' + profile][ind] == 1])
                for profile in profiles]
        return list(sets[0].intersection(*sets[1:]))

    def _filter_by_ege(ege):
        sets = [set([ind for ind in inds if 'name' in subj and 'min' in subj and 'max' in subj and subj['name'] in _ege
                     and subj['min'] <= _table['EGE_' + subj['name']][ind] <= subj['max']]) for subj in ege]
        return list(sets[0].intersection(*sets[1:]))

    def _filter_by_oge(oge):
        sets = [set([ind for ind in inds if 'name' in subj and 'min' in subj and 'max' in subj and subj['name'] in _ege
                     and subj['min'] <= _table['OGE_' + subj['name']][ind] <= subj['max']]) for subj in oge]
        return list(sets[0].intersection(*sets[1:]))

    if 'districts' in filters and len(filters['districts']) > 0:
        inds = _filter_by_district(filters['districts'])
    else:
        inds = list(range(len(_table)))
    if 'parallel' in filters:
        inds = _filter_by_class(filters['parallel'])
    if 'profiles' in filters and len(filters['profiles']) > 0:
        inds = _filter_by_profiles(filters['profiles'])
    if 'ege' in filters and len(filters['ege']) > 0:
        inds = _filter_by_ege(filters['ege'])
    if 'oge' in filters and len(filters['oge']) > 0:
        inds = _filter_by_oge(filters['oge'])
    return inds


def _to_json(d):
    return json.dumps(d, ensure_ascii=False, encoding='UTF-8')


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
        "stud_from": int(t.stud_from[0]),
        "stud_to": int(t.stud_to[0]),
        "profiles": _profiles_to_arr(t),
        "address": str(t.address[0]),
        "ogrn": str(t.ogrn[0]),
        "okato": str(t.okato[0]),
        "ou_type": str(t.ou_type[0]),
        "ou_class": str(t.ou_class[0]),
        "subjects_ege": {subj: float(t["EGE_" + subj][0]) for subj in _ege},
        "subjects_oge": {subj: float(t["OGE_" + subj][0]) for subj in _oge},
        "addresses": _addresses_to_arr(_addresses[_addresses.ekis_id == ekis_id]),
        "schools_like_this": [_get_school_pair(t['schools_like_this' + str(i)][0]) for i in range(1, 11)],
    }
    return res


def get_schools_by_string(string):
    res = []
    for i, name in enumerate(_table.name):
        if string in str(name):
            res.append(_get_school_short_ind(i))
    return res


def get_schools_filter(filters):
    """
    {
      "districts": [
        "Северо-Восточный",
        "Троицкий"
      ],
      "egeResults": [
        {
          "max": 78,
          "min": 26,
          "name": "Математика (профиль)"
        }
      ],
      "ogeResults": [
        {
          "max": 5,
          "min": 2,
          "name": "Математика"
        }
      ],
      "parallel": "10",
      "profiles": [
        "Естественно-научный",
        "Экономический"
      ]
    }
    """
    return _get_schools_short_ind(_filtering(json.loads(filters)))


def get_school_json(ekis_id):
    return json.dumps(get_school(ekis_id), ensure_ascii=False)


def get_schools_by_string_json(string):
    return json.dumps(get_schools_by_string(string), ensure_ascii=False)


def get_schools_filter_json(filters):
    return json.dumps(get_schools_filter(filters), ensure_ascii=False)


def get_lists():
    return json.dumps({
        'coordinates': _coordinates,
        'profiles': _profiles,
        'ege': _ege,
        'oge': _oge
    }, ensure_ascii=False)

