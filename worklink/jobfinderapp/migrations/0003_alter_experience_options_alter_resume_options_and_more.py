# Generated by Django 4.1.7 on 2023-04-01 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobfinderapp', '0002_resume_user_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experience',
            options={'verbose_name': 'Опыт работы', 'verbose_name_plural': 'Опыт работы'},
        ),
        migrations.AlterModelOptions(
            name='resume',
            options={'verbose_name': 'Резюме', 'verbose_name_plural': 'Резюме'},
        ),
        migrations.AlterField(
            model_name='resume',
            name='description',
            field=models.TextField(max_length=2048, verbose_name='описание'),
        ),
    ]