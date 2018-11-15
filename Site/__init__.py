from django.http import HttpResponse
from django.shortcuts import render


def main_page(request):
    return render(request, "main_page.html")


def school_info(request, id):
    return HttpResponse("There will be info about school")
