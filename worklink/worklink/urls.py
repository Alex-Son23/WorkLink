from worklink import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.IndexView.as_view()),

]
