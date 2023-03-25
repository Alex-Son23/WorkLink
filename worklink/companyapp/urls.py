from django.urls import path

from companyapp.views import VacancyView, vacancy, company, respond_to_vacancy

app_name = 'companyapp'

urlpatterns = [
    path('vacancies/', VacancyView.as_view(), name='vacancies'),
    path('vacancy/<int:pk>/', vacancy, name='vacancy'),
    path('<int:pk>/', company, name='company'),
    path('vacancy/<int:pk>/respond/', respond_to_vacancy, name='respond_to_vacancy')
]