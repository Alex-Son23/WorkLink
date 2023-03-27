from django.db import models
from authapp.models import CompanyProfile


class Vacancy(models.Model):
    title = models.CharField(max_length=256, verbose_name='название')
    position = models.CharField(max_length=256, verbose_name='должность')
    salary = models.PositiveIntegerField(verbose_name='зарплата')
    remote = models.BooleanField(default=False, verbose_name='удаленная')
    country = models.CharField(max_length=256, verbose_name='страна')
    city = models.CharField(max_length=256, verbose_name='город')
    is_closed = models.BooleanField(default=False, verbose_name='закрыто')
    description = models.CharField(max_length=2048, verbose_name='описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано', editable=False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='отредактировано', editable=False)
    company_id = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, verbose_name='компания')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return f'{self.title} - {self.company_id}'
