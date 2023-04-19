# Generated by Django 4.1.7 on 2023-04-19 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20230418_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('ожидание ответа', 'ожидание ответа'), ('отказ', 'отказ'), ('принято', 'принято'), ('cвяжусь в ближайшее время', 'cвяжусь в ближайшее время'), ('готов дать ответ через неделю', 'готов дать ответ через неделю'), ('готов дать ответ через меся', 'готов дать ответ через меся')], default='ожидание ответа', max_length=128, verbose_name='статус')),
            ],
        ),
        migrations.AlterField(
            model_name='offer',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.offerstatus', verbose_name='статус'),
        ),
    ]
