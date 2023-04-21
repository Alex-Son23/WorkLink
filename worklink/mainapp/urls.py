from django.urls import path
from mainapp.views import *

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
    path('my-vacancies/<int:pk>/responses/', VacancyResponsesListView.as_view(), name='vacancy_responses'),
    path('my-vacancies/<int:pk>/offers/', VacancyOffersListView.as_view(), name='vacancy_offers'),
    path('my-vacancies/<int:vacancy_id>/responses/<int:pk>/', VacancyResponseUpdateView.as_view(), name='vacancy_response_update'),
    path('my-vacancies/<int:vacancy_id>/offers/<int:pk>/', VacancyOfferUpdateView.as_view(), name='vacancy_offer_update'),

    path('vacancies/', VacancyView.as_view(), name='vacancies'),
    path('vacancy/<int:pk>/', vacancy, name='vacancy'),
    path('vacancy/<int:pk>/apply/', apply_to_vacancy, name='apply_to_vacancy'),
    path('<int:pk>/', company, name='company'),

    path('resumes/', ResumesAllListView.as_view(), name='resumes'),
    path('resume/<int:pk>/detail', ResumeDetailView.as_view(), name='resume_detail'),

    # response
    path('my-response/', ResponseListView.as_view(), name='my-response'),

    # offer
    path('my-offers/', OfferListView.as_view(), name='my-offer'),
    path('my-offers/<int:pk>/edit', OfferApplyView.as_view(), name='offer-edit'),

    path('resume/<int:pk>/apply/', apply_to_resume, name='apply_to_resume'),
]
