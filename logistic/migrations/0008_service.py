# Generated by Django 4.1.4 on 2023-01-07 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0007_rename_service_servicecategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('name_en', models.CharField(blank=True, max_length=100, null=True)),
                ('name_mn', models.CharField(blank=True, max_length=100, null=True)),
                ('description_uz', models.TextField(blank=True, max_length=3000, null=True)),
                ('description_ru', models.TextField(blank=True, max_length=3000, null=True)),
                ('description_en', models.TextField(blank=True, max_length=3000, null=True)),
                ('description_mn', models.TextField(blank=True, max_length=3000, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistic.servicecategory')),
            ],
        ),
    ]
