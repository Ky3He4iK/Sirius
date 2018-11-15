from django.http import HttpResponse


def main_page(request):

    return HttpResponse("This is main page")


def school_info(request, id):
    return HttpResponse("There will be info about school")
