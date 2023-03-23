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
    path('news/', views.NewsView.as_view(), name='news'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('job_listing/', views.JobListing.as_view(), name='job_listing'),
    path('job_form/', views.JobListing.as_view(), name='job_listing'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)