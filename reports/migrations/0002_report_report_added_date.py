# Generated by Django 3.1.5 on 2022-02-19 20:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='report_added_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date added'),
            preserve_default=False,
        ),
    ]
