from django.db import models

from authapp.models import CompanyProfile
from django.dispatch import receiver
from authapp.models import WorkLinkUser
from django.db.models.signals import post_save


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
    user = models.ForeignKey(WorkLinkUser, on_delete=models.CASCADE, verbose_name='пользователь')

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'

    def get_experience(self):
        return Experience.objects.filter(resume=self)

    def __str__(self):
        return f'{self.title}'


class Experience(models.Model):
    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'

    resume = models.ForeignKey(
        Resume, on_delete=models.CASCADE, verbose_name='резюме')
    company = models.ForeignKey(
        CompanyProfile, on_delete=models.CASCADE, verbose_name='компания')
    position = models.CharField(max_length=256, verbose_name='должность')
    description = models.CharField(max_length=2048, verbose_name='описание')
    start_date = models.DateField()
    end_date = models.DateField()

    def get_company_name(self):
        return CompanyProfile.objects.get(id=self.company.id).name


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
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, verbose_name='компания')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        # return f'{self.company}'
        return f'{self.title} - {self.company}'

    def responses(self):
        return Response.objects.filter(vacancy=self).all()

    def offers(self):
        return Offer.objects.filter(vacancy=self)

    def response_count(self):
        return len(self.responses())

    def offers_count(self):
        return len(self.offers())


class Status(models.Model):
    WAITING = 'ожидание ответа'
    REFUSAL = 'отказ'
    ACCEPT = 'принято'

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    STATUS_CHOISES = (
        (WAITING, 'Ожидание ответа'),
        (ACCEPT, 'Приглашение'),
        (REFUSAL, 'Отказ'),
    )

    title = models.CharField(choices=STATUS_CHOISES, default=WAITING, max_length=128, verbose_name='статус')

    @staticmethod
    def get_status_waiting():
        try:
            return Status.objects.get(title=Status.WAITING)
        except Status.DoesNotExist:
            return Status.objects.create(title=Status.WAITING)

    def __str__(self):
        return f'{self.title}'


class Offer(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, verbose_name='резюме')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, verbose_name='вакансия')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='статус')
    cover_letter = models.TextField(verbose_name='сопроводительное письмо')
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата')

    class Meta:
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'


class Response(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, verbose_name='резюме')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, verbose_name='вакансия')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='статус', null=True)
    cover_letter = models.TextField(verbose_name='сопроводительное письмо')
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата', null=True)

# @receiver(post_save, sender=Response)
# def create_user_profile(sender, instance, created, **kwargs):
#     instance.status = Status.objects.get(title='Ожидание ответа')
