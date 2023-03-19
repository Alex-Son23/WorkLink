from django.contrib import admin
#
from authapp.models import WorkLinkUser, JobFinderProfile, CompanyProfile
#
admin.site.register(WorkLinkUser)
admin.site.register(JobFinderProfile)
admin.site.register(CompanyProfile)
