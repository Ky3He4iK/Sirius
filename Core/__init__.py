import pandas as pd
import os
from django.conf import settings

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
