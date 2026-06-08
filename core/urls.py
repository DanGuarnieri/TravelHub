from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.trips.urls')),
    path('', include("apps.checklists.urls")),
    path('',include("apps.finances.urls")),
    path('',include("apps.documents.urls")),
    path('',include("apps.itineraries.urls")),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)