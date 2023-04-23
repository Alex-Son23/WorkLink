import adminapp.views as adminapp
from django.urls import path


app_name = 'adminapp'

urlpatterns = [
    path('vacancies/read/', adminapp.vacancies, name='vacancies'),
    path('vacancies/read/<int:pk>/', adminapp.vacancies_plus, name='vacancies_plus'),

]
