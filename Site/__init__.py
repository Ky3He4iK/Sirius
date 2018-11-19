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


def school_info(request, id):
    return HttpResponse("There will be info about school")


def humans(*_, **__):
    return HttpResponse(humans_page.replace('\n', '<br/>'))


def adv_search(request):
    return HttpResponse("There will be search")


def search(request):
    name = request.GET['s']
    return render(request, "index.html")


def search_results(request, payload):
    
    return render(request, "main_page.html")
