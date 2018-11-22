from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
import os
import json

import Core


humans_page = open(os.path.join(settings.STATIC_URL, "humans.txt")).read()
Core.lists.update({'classes': [i for i in range(1, 13)]})


def main_page(request):
    # try:
        if request.path == '/':
            return redirect("/main")
        if 's' in request.GET:
            return search(request)
        return render(request, "index.html", Core.lists)
    # except Exception as e:
    #     print(e, e.args)
    #     return HttpResponse("Err", status=500)


def humans(*_, **__):
    return HttpResponse(humans_page, content_type="text/plain")


def adv_search(request):
    # try:
        if 'data' in request.POST:
            data = Core.get_schools_filter(json.loads(request.POST['data']))
        elif 'filters' in request.GET:
            filters = json.loads(request.GET['filters'])
            data = Core.get_schools_filter(filters)
        else:
            return redirect("/main")
        response = render(request, "result.html", {'schools': data, 'count': len(data)})
        print("filters")
        return response
    # except Exception as e:
    #     print(e, e.args)
    #     return redirect("/main")


def search(request):
    # try:
        name = request.GET['s']
        data = Core.get_schools_by_string(name)
        res = render(request, "result.html", {'schools': data, 'count': len(data)})
        print("request")
        return res
    # except Exception as e:
    #     print(e, e.args)
    #     return redirect("/main")


def school(request):
    # try:
        if 'id' not in request.GET:
            return redirect("/main")
        school_inf = Core.get_school(int(request.GET['id']))
        if len(school_inf) == 0:
            return redirect("/main")
        # print(school_inf)
        return render(request, "school.html", school_inf)
    # except Exception as e:
    #     print(e, e.args)
    #     return redirect("/main")
