import datetime as dt

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render


def credits(request):
    content = "Nicky\nYour Name"
    return HttpResponse(content, content_type="text/plain")


def about(request):
    content = "<div>'Django in Action' book project</div>"
    return HttpResponse(content, content_type="text/html")


def version(request):
    content = {"version": "2"}
    return JsonResponse(content)


def news(request):
    data = {
        "news": [
            "RiffMates now has a news page!",
            "RiffMates has its first web page",
        ]
    }
    return render(request, "news.html", data)


def news_advanced(request):
    data = {
        "news": [
            (dt.datetime.now(), "RiffMates now has a news page!"),
            (dt.datetime.now(), "RiffMates has its first web page"),
            (dt.datetime.now(), "RiffMates has advanced news page"),
        ]
    }
    return render(request, "news_adv.html", data)
