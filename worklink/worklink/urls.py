from worklink import views
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    # закомментировать чтобы прошли миграции
    # path('admin/', admin.site.urls),

    path('', views.IndexView.as_view(), name='index'),
    path('auth/', include('authapp.urls', namespace='auth')),
]
