from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
import os

import Core

humans_page = open(os.path.join(settings.STATIC_URL, "humans.txt")).read()


def main_page(request):
    try:
        if request.path == '/':
            return redirect("/main")
        if 's' in request.GET:
            return search(request)
        return render(request, "index.html")
    except Exception as e:
        print(e, e.args)
        return redirect("/main")


def humans(*_, **__):
    return HttpResponse(humans_page, content_type="text/plain")


def adv_search(request):
    try:
        if request.method != 'POST' or 'data' not in request.POST:
            return redirect("/main")
        data = Core.get_schools_filter(request.POST['data'])
        return render(request, "result.html", data)
    except Exception as e:
        print(e, e.args)
        return redirect("/main")


def search(request):
    try:
        name = request.GET['s']
        data = Core.get_schools_by_string(name)
        return render(request, "result.html", data)
    except Exception as e:
        print(e, e.args)
        return redirect("/main")


def school(request):
    try:
        if 'id' not in request.GET:
            return redirect("/main")
        school_inf = Core.get_school(int(request.GET['id']))
        if len(school_inf) == 0:
            return redirect("/main")
        return render(request, "school.html", school_inf)
    except Exception as e:
        print(e, e.args)
        return redirect("/main")