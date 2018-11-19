import pandas as pd
from django.conf import settings
import json
import os

table = pd.read_csv(os.path.join(settings.BASE_DIR, "data/table.csv"), sep=';')


def _find_schools(name):
    return table['name'].str.contains(name, regex=False)


def simple_search(name):
    # TODO: remove redundant columns
    return table[_find_schools(name)]


def adv_search(**params):
    # TODO
    return []


def get_school(ekis_id):
    t = table[table.ekis_id == ekis_id]
    if len(t) == 0:
        return []
    return t.to_json(orient='records')


def get_schools_short(ekisis):
    t = []
    ekisis = set(ekisis)
    for ind in range(len(table)):
        if table[ind].ekis_id in ekisis:
            t.append(table[ind])
        pass
    return json.dumps(t)
