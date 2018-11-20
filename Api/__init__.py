from django.http import HttpResponse

import Core


def get_school(request):
    # try:
        if 'id' not in request.GET:
            return HttpResponse("I'm a teapot, I can't understand you", content_type="text/plain", status=418)
        return HttpResponse(Core.get_school_json(int(request.GET['id'])), content_type="application/json")
    # except Exception as e:
    #     print(e, e.args)
    #     return HttpResponse("An error occupied: " + str(e), content_type="text/plain", status=500)


def adv_search(request):
    # try:
        if request.method != 'POST' or "data" not in request.POST:
            return HttpResponse("I'm a teapot, I can't understand you", content_type="text/plain", status=418)
        return HttpResponse(Core.get_schools_filter_json(request.POST['data']), content_type="application/json")
    # except Exception as e:
    #     print(e, e.args)
    #     return HttpResponse("An error occupied: " + str(e), content_type="text/plain", status=500)


def search(request):
    # try:
        if "s" not in request.GET:
            return HttpResponse("I'm a teapot, I can't understand you", content_type="text/plain", status=418)
        return HttpResponse(Core.get_schools_by_string(request.GET['s']), content_type="application/json")
    # except Exception as e:
    #     print(e, e.args)
    #     return HttpResponse("An error occupied: " + str(e), content_type="text/plain", status=500)
