from django.urls import path
from jobfinderapp.views import ResumeListView, ResumeUpdateView, ResumeCreateView, delete_resume


app_name = "jobfinderapp"


urlpatterns = [
    path('my-resumes/', ResumeListView.as_view(), name='my-resumes'),
    path('my-resumes/<int:pk>/edit', ResumeUpdateView.as_view(), name='resume_edit'),
    path('my-resumes/add', ResumeCreateView.as_view(), name='resume_add'),
    path('my-resumes/<int:pk>/delete', delete_resume, name='resume_delete'),
]
