
from companyapp.views import VacancyListView, VacancyCreateView, VacancyDetailView, VacancyUpdateView, VacancyView, vacancy, company
from django.urls import path

app_name = "companyapp"

from django.urls import path

urlpatterns = [
    path('my-vacancies/', VacancyListView.as_view(), name='vacancies'),
    path('my-vacancies/add/', VacancyCreateView.as_view(), name='vacancy_add'),
    path('my-vacancies/<int:pk>/', VacancyDetailView.as_view(), name='vacancy_detail'),
    path('my-vacancies/<int:pk>/edit/', VacancyUpdateView.as_view(), name='vacancy_edit'),
    path('vacancies/', VacancyView.as_view(), name='vacancies'),
    path('vacancy/<int:pk>/', vacancy, name='vacancy'),
    path('<int:pk>/', company, name='company'),
    # path('vacancy/<int:pk>/respond/', respond_to_vacancy, name='respond_to_vacancy')
]

