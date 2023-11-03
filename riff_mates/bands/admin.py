from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from bands.filters import DecadeListFilter
from bands.models import Musician, Venue, Room
from bands.models import Band


def get_html(items, singular, plural):
    if not items:
        return format_html("<i>None</i>")

    plural = plural if len(items) > 1 else ""
    param = "?id__in=" + ",".join(str(item.id) for item in items)
    url = reverse(f"admin:bands_{singular}_changelist") + param

    return format_html('<a href="{}">{}{}</a>', url, singular.capitalize(), plural)


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ("id", "last_name", "first_name", "birth", "show_weekday", "show_bands")
    list_filter = (DecadeListFilter,)
    search_fields = ("last_name", "first_name")

    def show_weekday(self, obj):
        return obj.birth.strftime("%A")

    show_weekday.short_description = "Birth Weekday"

    def show_bands(self, obj):
        bands = obj.band_set.all()
        return get_html(bands, "band", "s")

    show_bands.short_description = "Bands"


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "show_members")
    search_fields = ("name",)

    def show_members(self, obj):
        members = obj.musicians.all()
        return get_html(members, "musician", "s")

    show_members.short_description = "Members"


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "show_rooms")
    search_fields = ("name",)

    def show_rooms(self, obj):
        rooms = obj.room_set.all()
        return get_html(rooms, "room", "s")

    show_rooms.short_description = "Rooms"


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
