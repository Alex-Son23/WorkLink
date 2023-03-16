from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timedelta

from django.dispatch import receiver
from django.db.models.signals import post_save

from django.utils.timezone import now


# шаблон абстрактного пользователя
class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст', default=18)


# модель профиля пользователя
class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж')
    )

    user = models.OneToOneField(
        User, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=64, verbose_name='номер телефона')
    gender = models.CharField(verbose_name='пол', choices=GENDER_CHOICES,
                              blank=True, max_length=1)
    birthday = models.DateField(verbose_name="день рождения")
    country = models.CharField(verbose_name='страна', max_length=64)
    city = models.CharField(verbose_name='город', max_length=64)
    is_employer = models.BooleanField(verbose_name='наниматель', default=True)





# class User(AbstractUser):
# avatar = models.ImageField(
#     upload_to='users_avatars',
#     blank=True
# )
# age = models.PositiveIntegerField(
#     verbose_name='возраст',
#     default=18
# )
#
# activation_key = models.CharField(
#     max_length=128,
#     blank=True
# )
# activation_key_expires = models.DateTimeField(
#     default=(now() + timedelta(hours=48))
# )

# def is_activation_key_expired(self):
#     if now() <= self.activation_key_expires:
#         return False
#     else:
#         return True


# class ShopUserProfile(models.Model):
#     MALE = 'M'
#     FEMALE = 'W'
#
#     GENDER_CHOICES = (
#         (MALE, 'М'),
#         (FEMALE, 'Ж')
#     )
#
#     user = models.OneToOneField(
#         User,
#         unique=True,
#         null=False,
#         db_index=True,
#         on_delete=models.CASCADE
#     )
#
#     tagline = models.CharField(
#         verbose_name='тэги',
#         max_length=128,
#         blank=True
#     )
#
#     about_me = models.TextField(
#         verbose_name='о себе',
#         max_length=512,
#         blank=True
#     )
#
#     gender = models.CharField(
#         verbose_name='пол',
#         choices=GENDER_CHOICES,
#         blank=True,
#         max_length=1
#     )
#
#     @receiver(post_save, sender=User)
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             User.objects.create(user=instance)
#
#     @receiver(post_save, sender=User)
#     def save_user_profile(sender, instance, **kwargs):
#         instance.shopuserprofile.save()
