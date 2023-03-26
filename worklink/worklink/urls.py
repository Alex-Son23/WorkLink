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

    # Вакансии
    path('job_list/', views.JobListView.as_view(), name='job_list'),
    path('job_form/', views.JobFormView.as_view(), name='job_form'),
    path('job_list/<int:pk>/', views.JobDetailView.as_view(), name='job_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)