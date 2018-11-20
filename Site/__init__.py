from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
import os

import Core

humans_page = open(os.path.join(settings.STATIC_URL, "humans.txt")).read()


def main_page(request):
    if request.path == '/':
        return redirect("/main")
    if 's' in request.GET:
        return search(request)
    return render(request, "index.html")


def humans(*_, **__):
    return HttpResponse(humans_page, content_type="text/plain")


def adv_search(request):
    if request.method != 'POST' or 'data' not in request.POST:
        return redirect("/main")
    data = Core.get_schools_filter(request.POST['data'])
    return render(request, "result.html", data)


def search(request):
    name = request.GET['s']
    data = Core.get_schools_by_string(name)
    return render(request, "result.html", data)


def school(request):
    if 'id' not in request.GET:
        return redirect("/main")
    school_inf = Core.get_school(int(request.GET['id']))
    if len(school_inf) == 0:
        return redirect("/main")
    return render(request, "school.html", school_inf)
