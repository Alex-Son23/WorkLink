from django.db import models
from django.contrib.auth.models import AbstractUser

from django.dispatch import receiver
from django.db.models.signals import post_save


# шаблон абстрактного пользователя
class WorkLinkUser(AbstractUser):
    JOB_FINDER = 'соискатель'
    COMPANY = 'компания'

    STATUS_CHOICES = (
        (JOB_FINDER, 'Cоискатель'),
        (COMPANY, 'Компания')
    )

    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    status = models.CharField(verbose_name='статус пользователя', choices=STATUS_CHOICES, blank=False, max_length=16)
    moderator = models.BooleanField(default=False)

    def get_company(self):
        return CompanyProfile.objects.filter(user=self).first()


# модель профиля пользователя
class JobFinderProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж')
    )

    user = models.OneToOneField(
        WorkLinkUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32, verbose_name='имя', blank=True)
    last_name = models.CharField(max_length=32, verbose_name='фамилия', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст', default=18, blank=True)
    phone = models.CharField(max_length=64, verbose_name='номер телефона', blank=True)
    gender = models.CharField(verbose_name='пол', choices=GENDER_CHOICES,
                              blank=True, max_length=1)
    birthday = models.DateField(verbose_name="день рождения", blank=True, null=True)
    country = models.CharField(verbose_name='страна', max_length=64, blank=True)
    city = models.CharField(verbose_name='город', max_length=64, blank=True)

    def __str__(self):
        return f'Profile {self.user}'


class CompanyProfile(models.Model):
    user = models.OneToOneField(
        WorkLinkUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, verbose_name='название компании')
    phone = models.CharField(max_length=64, verbose_name='номер телефона', blank=True)
    country = models.CharField(verbose_name='страна', max_length=64, blank=True)
    city = models.CharField(verbose_name='город', max_length=64, blank=True)
    description = models.CharField(verbose_name='описание', max_length=512, blank=True)
    greeting_letter = models.CharField(verbose_name='приветственное письмо', max_length=512, blank=True)
    is_partner = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f'Company {self.user}'


@receiver(post_save, sender=WorkLinkUser)
def create_user_profile(sender, instance, created, **kwargs):
    user = instance
    if created and instance.status == 'соискатель':
        profile = JobFinderProfile.objects.create(user=user)
        profile.save()
    elif created and instance.status == 'компания':
        company = CompanyProfile.objects.create(user=user)
        company.save()
