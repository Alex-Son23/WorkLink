from django.urls import path
from mainapp.views import ResumeListView, ResumeUpdateView, ResumeCreateView, delete_resume, VacancyListView, \
    VacancyCreateView, VacancyDetailView, VacancyUpdateView, VacancyView, vacancy, company

app_name = "mainapp"

urlpatterns = [
    path('my-resumes/', ResumeListView.as_view(), name='my-resumes'),
    path('my-resumes/<int:pk>/edit', ResumeUpdateView.as_view(), name='resume_edit'),
    path('my-resumes/add', ResumeCreateView.as_view(), name='resume_add'),
    path('my-resumes/<int:pk>/delete', delete_resume, name='resume_delete'),

    path('my-vacancies/', VacancyListView.as_view(), name='my-vacancies'),
    path('my-vacancies/add/', VacancyCreateView.as_view(), name='vacancy_add'),
    path('my-vacancies/<int:pk>/', VacancyDetailView.as_view(), name='vacancy_detail'),
    path('my-vacancies/<int:pk>/edit/', VacancyUpdateView.as_view(), name='vacancy_edit'),
    path('vacancies/', VacancyView.as_view(), name='vacancies'),
    path('vacancy/<int:pk>/', vacancy, name='vacancy'),
    path('<int:pk>/', company, name='company'),
]
