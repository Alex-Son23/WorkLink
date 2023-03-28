from companyapp.views import VacancyListView, VacancyCreateView, VacancyDetailView, VacancyUpdateView

app_name = "companyapp"

from django.urls import path

urlpatterns = [
    path('vacancies/', VacancyListView.as_view(), name='vacancies'),
    path('vacancies/add/', VacancyCreateView.as_view(), name='vacancy_add'),
    path('vacancies/<int:pk>/', VacancyDetailView.as_view(), name='vacancy_detail'),
    path('vacancies/<int:pk>/edit/', VacancyUpdateView.as_view(), name='vacancy_edit'),
]
