# Generated by Django 4.1.7 on 2023-03-26 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_alter_companyprofile_is_partner'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')),
                ('deleted', models.BooleanField(default=False, verbose_name='удалено')),
                ('title', models.CharField(max_length=64, verbose_name='название вакансии')),
                ('celery', models.PositiveIntegerField(verbose_name='зарплата')),
                ('body', models.TextField(verbose_name='описание вакансии')),
                ('body_as_markdown', models.BooleanField(default=False, verbose_name='способ разметки')),
            ],
            options={
                'verbose_name': 'вакансия',
                'verbose_name_plural': 'вакансии',
            },
        ),
    ]