# Generated by Django 4.1.7 on 2023-03-28 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companyapp', '0002_alter_vacancy_company_id_delete_company'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancy',
            options={'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
    ]
