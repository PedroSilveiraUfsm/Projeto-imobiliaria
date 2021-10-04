from django.urls import path, include
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Sistema Imobiliária"
admin.site.site_title = "Portal da Administração"
admin.site.index_title = "Imobiliária - Controle de Agenda"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('agenda.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)