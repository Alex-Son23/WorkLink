from django.urls import path

from companyapp.views import VacancyView, vacancy, company

app_name = 'companyapp'

urlpatterns = [
    path('vacancies/', VacancyView.as_view(), name='vacancies'),
    path('vacancy/<int:pk>/', vacancy, name='vacancy'),
    path('<int:pk>/', company, name='company'),
]