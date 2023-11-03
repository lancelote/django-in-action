from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from bands.filters import DecadeListFilter
from bands.models import Musician, Venue, Room
from bands.models import Band


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

        if not bands:
            return format_html("<i>None</i>")

        plural = "s" if len(bands) > 1 else ""
        param = "?id__in=" + ",".join(str(band.id) for band in bands)
        url = reverse("admin:bands_band_changelist") + param

        return format_html('<a href="{}">Band{}</a>', url, plural)

    show_bands.short_description = "Bands"


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "show_members")
    search_fields = ("name",)

    def show_members(self, obj):
        members = obj.musicians.all()

        if not members:
            return format_html("<i>None</i>")

        plural = "s" if len(members) > 1 else ""
        param = "?id__in=" + ",".join(str(member.id) for member in members)
        url = reverse("admin:bands_musician_changelist") + param

        return format_html('<a href="{}">Member{}</a>', url, plural)

    show_members.short_description = "Members"


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
