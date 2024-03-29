# Generated by Django 4.1.7 on 2023-04-19 08:46

from django.db import migrations



def populate_statuses(apps, schema_editor):
    Status = apps.get_model('mainapp', 'Status')
    statuses = (item.title for item in Status.objects.all())
    for item, _ in Status.title.field.choices:
        if item not in statuses:
            Status.objects.create(title=item)



class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_statuses)
    ]
