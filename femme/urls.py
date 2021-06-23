from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^',include('web.urls',namespace="web")),
   
    
    url(r'^media/(?P<path>.*)$', serve, { 'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, { 'document_root': settings.STATIC_FILE_ROOT}),
    
]
