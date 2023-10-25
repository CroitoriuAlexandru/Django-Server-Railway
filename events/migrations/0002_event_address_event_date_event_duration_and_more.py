# Generated by Django 4.0.4 on 2023-10-23 13:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='event',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='servicereview',
            name='review',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='servicereview',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
