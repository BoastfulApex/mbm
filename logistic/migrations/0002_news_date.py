# Generated by Django 4.1.4 on 2022-12-12 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
