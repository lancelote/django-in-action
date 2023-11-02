from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from bands.models import Band
from bands.models import Musician
from bands.models import Room
from bands.models import Venue

DEFAULT_PER_PAGE = 2
MAXIMUM_PER_PAGE = 5


def musician(request, musician_id):
    data = {"musician": get_object_or_404(Musician, id=musician_id)}
    return render(request, "musician.html", data)


def band(request, band_id):
    data = {"band": get_object_or_404(Band, id=band_id)}
    return render(request, "band.html", data)


def venue(request, venue_id):
    data = {"venue": get_object_or_404(Venue, id=venue_id)}
    return render(request, "venue.html", data)


def room(request, room_id):
    data = {"room": get_object_or_404(Room, id=room_id)}
    return render(request, "room.html", data)


def get_items_per_page(request):
    per_page = int(request.GET.get("per_page", DEFAULT_PER_PAGE))

    if per_page < 1:
        per_page = DEFAULT_PER_PAGE
    elif per_page > 5:
        per_page = MAXIMUM_PER_PAGE

    return per_page


def get_page_num(request, paginator):
    page_num = int(request.GET.get("page", 1))

    if page_num < 1:
        page_num = 1
    elif page_num > paginator.num_pages:
        page_num = paginator.num_pages

    return page_num


def get_page(request, items):
    per_page = get_items_per_page(request)
    paginator = Paginator(items, per_page)
    page_num = get_page_num(request, paginator)
    return paginator.page(page_num)


def musicians(request):
    all_musicians = Musician.objects.all().order_by("last_name")
    page = get_page(request, all_musicians)
    return render(request, "musicians.html", {"musicians": page.object_list, "page": page})


def bands(request):
    all_bands = Band.objects.all().order_by("name")
    page = get_page(request, all_bands)
    return render(request, "bands.html", {"bands": page.object_list, "page": page})


def venues(request):
    all_venues = Venue.objects.all().order_by("name")
    page = get_page(request, all_venues)
    return render(request, "venues.html", {"venues": page.object_list, "page": page})
