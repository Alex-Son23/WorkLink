from django.contrib import admin
from authapp.models import WorkLinkUser, JobFinderProfile
from authapp.models import CompanyProfile

admin.site.register(WorkLinkUser)
admin.site.register(JobFinderProfile)
admin.site.register(CompanyProfile)
