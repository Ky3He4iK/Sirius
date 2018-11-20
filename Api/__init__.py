from django.http import HttpResponse

import Core

template_response_get = '''
{
    "name": "№123"
    "name_full": "№123(321)",
    "site": "nan",
    "email": "qwe@ewq.as",
    "phone": "nan",
    "principal": "AAA",
    "stud_from": 1,
    "stud_to": 2,
    "prophiles": [
        "Технический"
    ],
    "address": "Ул. Пушкина, д. Колотушкина",
    "ogrn": 88005553535,
    "okato": 53535550088,
    "financing": "Негосударственное",
    "ou_type": "Общеобразовательное учереждение",
    "ou_class": "Детский сад",
    "ege_mean": 5,
    "subjects_ege": {"Математика": 123},
    "subjects_oge": {},
    "addresses": [
        {
            "isMain": True,
            "fullname": "Ул. Пушкина, д. Колотушкина",
            "latLng": [1, -1]
        }
    ],
    "schools_like_this": [
        [123, "№123"],
        [123, "№123"],
        [123, "№123"],
        [123, "№123"],
        [123, "№123"],
        [123, "№123"],
        [123, "№123"],
        [123, "№123"],
        [123, "№123"],
        [123, "№123"]
    ]
}
'''

template_response_search = '''
[
    {
        "lat": [55.55, 54.45, 64.2],
        "long": [37.43, 34.3, 35.5],
        "name": "ПТУ №314",
        "addresses": ["ул. Пушкина, д. Колотушкина", "Кремль", "Коробка под мостом"],
        "from": 5,
        "to": 11,
        "director": "Владимир Владимирович",
        "email": "vova@example.com",
        "to_be_continued": true
    },
    {
        "lat": [52.55],
        "long": [35.43],
        "name": "Колледж №152",
        "addresses": ["Южное Бутово"],
        "from": 11,
        "to": 11,
        "director": "Дмитрий Анатольевич",
        "email": "syn_podrugi@example.com",
        "to_be_continued": true
    },
]
'''


def get_school(request):
    if 'id' not in request.GET:
        return HttpResponse("I'm a teapot, I can't understand you", content_type="text/plain", status=418)
    return HttpResponse(Core.get_school_json(int(request.GET['id'])), content_type="application/json")


def adv_search(request):
    if request.method != 'POST' or "data" not in request.POST:
        return HttpResponse("I'm a teapot, I can't understand you", content_type="text/plain", status=418)
    return HttpResponse(Core.get_schools_filter_json(request.POST['data']), content_type="application/json")


def search(request):
    if "s" not in request.GET:
        return HttpResponse("I'm a teapot, I can't understand you", content_type="text/plain", status=418)
    return HttpResponse(Core.get_schools_by_string(request.GET['s']), content_type="application/json")
