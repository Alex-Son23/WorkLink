# Generated by Django 4.1.7 on 2023-04-01 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authapp', '0005_delete_joblist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='название')),
                ('position', models.CharField(max_length=256, verbose_name='должность')),
                ('salary', models.PositiveIntegerField(verbose_name='зарплата')),
                ('relocate', models.BooleanField(default=False, verbose_name='возможность переезда')),
                ('remote', models.BooleanField(default=False, verbose_name='удаленная')),
                ('visible', models.BooleanField(default=False, verbose_name='видимость')),
                ('is_draft', models.BooleanField(default=False, verbose_name='черновик')),
                ('description', models.CharField(max_length=2048, verbose_name='описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='отредактировано')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=256, verbose_name='должность')),
                ('description', models.CharField(max_length=2048, verbose_name='описание')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authapp.companyprofile', verbose_name='компания')),
                ('resume_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobfinderapp.resume', verbose_name='резюме')),
            ],
        ),
    ]