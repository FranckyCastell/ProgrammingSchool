from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('HomeApp.urls')),
    path('', include('CoursesApp.urls')),
    path('', include('ContactApp.urls')),
    path('', include('CalendarApp.urls')),
    path('', include('AboutApp.urls')),
    path('', include('RegisterApp.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
