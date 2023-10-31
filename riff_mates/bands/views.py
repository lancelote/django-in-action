from django.shortcuts import render
from django.shortcuts import get_object_or_404

from bands.models import Musician


def musician(request, musician_id):
    data = {"musician": get_object_or_404(Musician, id=musician_id)}
    return render(request, "musician.html", data)
