from django.http import HttpResponse
from django.http import JsonResponse


def credits(request):
    content = "Nicky\nYour Name"
    return HttpResponse(content, content_type="text/plain")


def about(request):
    content = "<div>'Django in Action' book project</div>"
    return HttpResponse(content, content_type="text/html")


def version(request):
    content = {"version": "2"}
    return JsonResponse(content)
