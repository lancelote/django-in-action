from django.contrib import admin

from bands.models import Musician


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ("id", "last_name", "first_name", "show_weekday")
    search_fields = ("last_name", "first_name")

    def show_weekday(self, obj):
        return obj.birth.strftime("%A")

    show_weekday.short_description = "Birth Weekday"
