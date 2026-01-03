
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
#이미지 업로드->media서빙 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('idea_site.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)