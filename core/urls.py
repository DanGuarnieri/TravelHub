from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. Rota raiz (redireciona para login)
    path('', RedirectView.as_view(pattern_name='login', permanent=False), name='home'),
    
    # 2. Rotas dos aplicativos com prefixos claros
    path('contas/', include('apps.accounts.urls')),
    path('viagens/', include('apps.trips.urls')),
    path('checklists/', include("apps.checklists.urls")),
    path('financas/', include("apps.finances.urls")),
    path('documentos/', include("apps.documents.urls")),
    path('roteiros/', include("apps.itineraries.urls")),
    path('galeria/', include("apps.gallery.urls")),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)