from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
import os

urlpatterns = [
    path('', include('perfil.urls_landing')),
    path('admin/', admin.site.urls),
    path('auth/', include('perfil.auth_urls')),
    path('perfil/', include('perfil.urls')),
    path('extrato/', include('extrato.urls')),
    path('planejamento/', include('planejamento.urls')),
    path('contas/', include('contas.urls')),
    path('blog/', include('blog.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    path('svg/<path:path>', serve, {'document_root': os.path.join(settings.BASE_DIR, 'svg')}),
]