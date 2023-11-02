import datetime as dt

from django.contrib import admin

from bands.models import Musician
from bands.models import Band


class DecadeListFilter(admin.SimpleListFilter):
    title = 'decade born'
    parameter_name = 'decade'

    def lookups(self, request, model_admin):
        result = []

        this_year = dt.datetime.today().year
        this_decade = (this_year // 10) * 10
        start = this_decade - 10

        for year in range(start, start - 100, -10):
            result.append((str(year), f"{year}-{year + 9}"))

        return result

    def queryset(self, request, queryset):
        start = self.value()

        if start is None:
            return queryset

        start = int(start)

        result = queryset.filter(
            birth__gte=dt.date(start, 1, 1),
            birth__lte=dt.date(start + 9, 12, 31),
        )

        return result


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ("id", "last_name", "first_name", "birth", "show_weekday")
    list_filter = (DecadeListFilter,)
    search_fields = ("last_name", "first_name")

    def show_weekday(self, obj):
        return obj.birth.strftime("%A")

    show_weekday.short_description = "Birth Weekday"


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    pass
