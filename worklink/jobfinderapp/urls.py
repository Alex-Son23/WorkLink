from django.urls import path

import jobfinderapp.views as jobfinderapp

app_name = 'jobfinderapp'

urlpatterns = [
    path('job-listing/', jobfinderapp.JobListingView.as_view(), name='job-listing'),
    
]
