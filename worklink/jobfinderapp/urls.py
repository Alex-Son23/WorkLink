from django.urls import path
from jobfinderapp.views import ResumeListView, ResumeUpdateView, ResumeCreateView


app_name = "jobfinderapp"


urlpatterns = [
    path('my-resumes/', ResumeListView.as_view(), name='my-resumes'),
    path('my-resumes/<int:pk>/edit', ResumeUpdateView.as_view(), name='resume_edit'),
    path('my-resumes/add', ResumeCreateView.as_view(), name='resume_add'),

]
