from worklink import views
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static

from worklink import settings

urlpatterns = [
    # закомментировать чтобы прошли миграции
    path('admin/', admin.site.urls),

    path('', views.IndexView.as_view(), name='index'),
    path('auth/', include('authapp.urls', namespace='auth')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)