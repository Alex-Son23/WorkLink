from django.db import models

from authapp.models import CompanyProfile
from authapp.models import WorkLinkUser


class Resume(models.Model):
    title = models.CharField(max_length=256, verbose_name='название')
    position = models.CharField(max_length=256, verbose_name='должность')
    salary = models.PositiveIntegerField(verbose_name='зарплата')
    relocate = models.BooleanField(
        default=False, verbose_name='возможность переезда')
    remote = models.BooleanField(default=False, verbose_name='удаленная')
    visible = models.BooleanField(default=False, verbose_name='видимость')
    is_draft = models.BooleanField(default=False, verbose_name='черновик')
    description = models.TextField(max_length=2048, verbose_name='описание')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='создано', editable=False)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='отредактировано', editable=False)
    user_id = models.ForeignKey(WorkLinkUser, on_delete=models.CASCADE, verbose_name='пользователь')

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'

    def get_experience(self):
        return Experience.objects.filter(resume_id=self)

    def __str__(self):
        return f'{self.title}'


class Experience(models.Model):
    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'

    resume_id = models.ForeignKey(
        Resume, on_delete=models.CASCADE, verbose_name='резюме')
    company_id = models.ForeignKey(
        CompanyProfile, on_delete=models.CASCADE, verbose_name='компания')
    position = models.CharField(max_length=256, verbose_name='должность')
    description = models.CharField(max_length=2048, verbose_name='описание')
    start_date = models.DateField()
    end_date = models.DateField()

    def get_company_name(self):
        return CompanyProfile.objects.get(id=self.company_id.id).name


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