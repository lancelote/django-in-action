import datetime as dt

from django.contrib import admin


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
