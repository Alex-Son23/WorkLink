from django.urls import re_path
from django.contrib import admin
from worklink.views import index

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^$", index, name='main'),
]
