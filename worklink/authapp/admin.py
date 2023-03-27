from django.contrib import admin
from authapp.models import WorkLinkUser, JobFinderProfile
from authapp.models import CompanyProfile
from companyapp.models import JobList

admin.site.register(WorkLinkUser)
admin.site.register(JobFinderProfile)
admin.site.register(CompanyProfile)


# Более информативный вывод новостей в админке
@admin.register(JobList)
class JobsAdmin(admin.ModelAdmin):
    # Отображение
    list_display = ('pk', 'title', 'deleted',)
    # Сортировка
    ordering = ('pk',)
    # Пагинация
    list_per_page = 5
    # Фильтрация
    list_filter = ('deleted', 'created_at',)
    # Поиск по тексту
    search_fields = ('title', 'body',)
    # Дополнительные опции (кастомизация)
    actions = ('mark_as_delete',)

    def mark_as_delete(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_delete.short_description = 'Пометить удаленным'
