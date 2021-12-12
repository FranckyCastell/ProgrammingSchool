from django.contrib import admin
from CalendarApp.models import Event

# Register your models here.


class CalendarAdmin(admin.ModelAdmin):
    list_display = ['title', 'start', 'end']  # COL DATA
    search_fields = ['title']  # SEARCH DATA



admin.site.register(Event, CalendarAdmin)