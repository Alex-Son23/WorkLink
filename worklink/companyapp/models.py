# Модель списка вакансий
from django.db import models
from authapp.models import BaseModel, JobsManager


class JobList(BaseModel):
    objects = JobsManager()

    title = models.CharField(max_length=64, verbose_name='название вакансии')
    celery = models.PositiveIntegerField(verbose_name='зарплата')
    body = models.TextField(verbose_name='описание вакансии')
    body_as_markdown = models.BooleanField(default=False, verbose_name='способ разметки')

    def __str__(self):
        return f'#{self.pk} {self.title}'

    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'
