# Generated by Django 4.1.4 on 2022-12-11 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField()),
                ('comment_uz', models.TextField(blank=True, max_length=3000, null=True)),
                ('comment_ru', models.TextField(blank=True, max_length=3000, null=True)),
                ('comment_en', models.TextField(blank=True, max_length=3000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_uz', models.TextField(blank=True, max_length=3000, null=True)),
                ('question_ru', models.TextField(blank=True, max_length=3000, null=True)),
                ('question_en', models.TextField(blank=True, max_length=3000, null=True)),
                ('answer_uz', models.TextField(blank=True, max_length=3000, null=True)),
                ('answer_ru', models.TextField(blank=True, max_length=3000, null=True)),
                ('answer_en', models.TextField(blank=True, max_length=3000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('name_en', models.CharField(blank=True, max_length=100, null=True)),
                ('description_uz', models.TextField(blank=True, max_length=3000, null=True)),
                ('description_ru', models.TextField(blank=True, max_length=3000, null=True)),
                ('description_en', models.TextField(blank=True, max_length=3000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=100, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=100, null=True)),
                ('name_en', models.CharField(blank=True, max_length=100, null=True)),
                ('description_uz', models.TextField(blank=True, max_length=3000, null=True)),
                ('description_ru', models.TextField(blank=True, max_length=3000, null=True)),
                ('description_en', models.TextField(blank=True, max_length=3000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
