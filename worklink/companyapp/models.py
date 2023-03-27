# Модель списка вакансий
from django.db import models


# Базовая модель
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')
    deleted = models.BooleanField(default=False, verbose_name='удалено')

    class Meta:
        abstract = True
        ordering = ('-created_at',)

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()


# Менеджер объекта
class JobsManager(models.Manager):

    def delete(self):
        pass

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


# Модель списка вакансий
class VacancyListModel(BaseModel):
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
