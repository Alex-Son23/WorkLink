from companyapp.views import VacancyListView, VacancyFormView, VacancyDetailView, VacancyUpdateView
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
    path('vacancies/', VacancyListView.as_view(), name='vacancies'),
    path('vacancies/add/', VacancyFormView.as_view(), name='vacancy_add'),
    path('vacancies/<int:pk>/', VacancyDetailView.as_view(), name='vacancy_detail'),
    path('vacancies/<int:pk>/edit/', VacancyUpdateView.as_view(), name='vacancy_edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
