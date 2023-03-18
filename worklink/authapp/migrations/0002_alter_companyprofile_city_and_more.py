# Generated by Django 4.1.7 on 2023-03-17 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='city',
            field=models.CharField(blank=True, max_length=64, verbose_name='город'),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='country',
            field=models.CharField(blank=True, max_length=64, verbose_name='страна'),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='description',
            field=models.CharField(blank=True, max_length=512, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='greeting_letter',
            field=models.CharField(blank=True, max_length=512, verbose_name='приветственное письмо'),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=64, verbose_name='номер телефона'),
        ),
        migrations.AlterField(
            model_name='jobfinderprofile',
            name='age',
            field=models.PositiveIntegerField(blank=True, default=18, verbose_name='возраст'),
        ),
        migrations.AlterField(
            model_name='jobfinderprofile',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='день рождения'),
        ),
        migrations.AlterField(
            model_name='jobfinderprofile',
            name='city',
            field=models.CharField(blank=True, max_length=64, verbose_name='город'),
        ),
        migrations.AlterField(
            model_name='jobfinderprofile',
            name='country',
            field=models.CharField(blank=True, max_length=64, verbose_name='страна'),
        ),
        migrations.AlterField(
            model_name='jobfinderprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=32, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='jobfinderprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=32, verbose_name='фамилия'),
        ),
        migrations.AlterField(
            model_name='jobfinderprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=64, verbose_name='номер телефона'),
        ),
        migrations.AlterField(
            model_name='worklinkuser',
            name='status',
            field=models.CharField(choices=[('соискатель', 'Cоискатель'), ('компания', 'Компания')], max_length=16, verbose_name='статус пользователя'),
        ),
    ]
