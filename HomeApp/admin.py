from django.contrib import admin
from HomeApp.models import ProgrammingLanguage, Users

# Register your models here.


class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ['name']  # COL DATA
    search_fields = ['name']  # SEARCH DATA


class UsersAdmin(admin.ModelAdmin):
    list_display = ['name', 'language']  # COL DATA
    search_fields = ['name', 'language__name']  # SEARCH DATA


admin.site.register(ProgrammingLanguage, ProgrammingLanguageAdmin)

admin.site.register(Users, UsersAdmin)
