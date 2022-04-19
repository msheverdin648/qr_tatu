from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('personal.urls')),
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]


if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)