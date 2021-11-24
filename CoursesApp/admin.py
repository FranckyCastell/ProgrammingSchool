from django.contrib import admin
from CoursesApp.models import Categories, Courses

# Register your models here.


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']  # COL DATA
    search_fields = ['name']  # SEARCH DATA


class CoursesAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']  # READ FIELDS
    list_display = ['title', 'author', 'category', 'price', 'updated']  # COL DATA
    search_fields = ['title', 'author__username', 'category__name']  # SEARCH DATA
    list_filter = ['author__username', 'category__name']  # FILTER



admin.site.register(Categories, CategoriesAdmin)

admin.site.register(Courses, CoursesAdmin)
