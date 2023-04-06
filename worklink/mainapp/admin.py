from django.contrib import admin
from mainapp.models import Resume, Experience, Vacancy

admin.site.register(Resume)
admin.site.register(Experience)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    # Отображение
    list_display = ('pk', 'title', 'position', 'salary', 'is_closed', 'created_at')
    ordering = ('pk',)
    list_per_page = 10
    list_filter = ('is_closed', 'created_at', 'company_id')
    search_fields = ('title', 'description', 'position')
    list_display_links = ('title',)
