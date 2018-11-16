from django.http import HttpResponse

template_response_get = '''
[
    {
        "lat": [55.55, 54.45, 64.2],
        "long": [37.43, 34.3, 35.5],
        "name": "ПТУ №%s",
        "addresses": ["ул. Пушкина, д. Колотушкина", "Кремль", "Коробка под мостом"],
        "ege": {
            "Математика": 99.9,
            "Русский": 1.2
        },
        "from": 5,
        "to": 11,
        "director": "Владимир Владимирович",
        "email": "vova@example.com",
        "to_be_continued": true
    }
]
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
    return HttpResponse(template_response_get % str(request.GET['id']), content_type="application/json")


def search(request):
    if request.method != 'POST':
        return HttpResponse("POST only", content_type="text/plain", status=405)
    return HttpResponse(template_response_search, content_type="application/json")
