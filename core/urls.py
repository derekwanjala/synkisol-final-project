from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('project/', include('project.urls', namespace='project')),

    path('service', views.service, name='service'),    
    path('<slug:slug>/', views.ServiceDetail.as_view(), name='service_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)