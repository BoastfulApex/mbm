from django.db import models


class Slider(models.Model):
    name_uz = models.CharField(max_length=100, null=True, blank=True)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    name_mn = models.CharField(max_length=100, null=True, blank=True)
    description_uz = models.TextField(max_length=3000, null=True, blank=True)
    description_ru = models.TextField(max_length=3000, null=True, blank=True)
    description_en = models.TextField(max_length=3000, null=True, blank=True)
    description_mn = models.TextField(max_length=3000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    link = models.URLField(null=True)

class News(models.Model):
    name_uz = models.CharField(max_length=100, null=True, blank=True)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    name_mn = models.CharField(max_length=100, null=True, blank=True)    
    date = models.DateField(null=True, blank=True)
    description_uz = models.TextField(max_length=3000, null=True, blank=True)
    description_ru = models.TextField(max_length=3000, null=True, blank=True)
    description_en = models.TextField(max_length=3000, null=True, blank=True)
    description_mn = models.TextField(max_length=3000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


class ServiceCategory(models.Model):
    name_uz = models.CharField(max_length=100, null=True, blank=True)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    name_mn = models.CharField(max_length=100, null=True, blank=True)
    
    description_uz = models.TextField(max_length=3000, null=True, blank=True)
    description_ru = models.TextField(max_length=3000, null=True, blank=True)
    description_en = models.TextField(max_length=3000, null=True, blank=True)
    description_mn = models.TextField(max_length=3000, null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)


class Service(models.Model):
    name_uz = models.CharField(max_length=100, null=True, blank=True)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    name_mn = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    description_uz = models.TextField(max_length=3000, null=True, blank=True)
    description_ru = models.TextField(max_length=3000, null=True, blank=True)
    description_en = models.TextField(max_length=3000, null=True, blank=True)
    description_mn = models.TextField(max_length=3000, null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)


class FAQ(models.Model):
    question_uz = models.TextField(max_length=3000, null=True, blank=True)
    question_ru = models.TextField(max_length=3000, null=True, blank=True)
    question_en = models.TextField(max_length=3000, null=True, blank=True)
    question_mn = models.TextField(max_length=3000, null=True, blank=True)
    answer_uz = models.TextField(max_length=3000, null=True, blank=True)
    answer_ru = models.TextField(max_length=3000, null=True, blank=True)
    answer_en = models.TextField(max_length=3000, null=True, blank=True)
    answer_mn = models.TextField(max_length=3000, null=True, blank=True)


class Comment(models.Model):
    author = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField()
    comment_uz = models.TextField(max_length=3000, null=True, blank=True)
    comment_ru = models.TextField(max_length=3000, null=True, blank=True)
    comment_en = models.TextField(max_length=3000, null=True, blank=True)
    comment_mn = models.TextField(max_length=3000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

class Partner(models.Model):
    name_uz = models.CharField(max_length=100, null=True, blank=True)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    name_mn = models.CharField(max_length=100, null=True, blank=True)    
    description_uz = models.TextField(max_length=3000, null=True, blank=True)
    description_ru = models.TextField(max_length=3000, null=True, blank=True)
    description_en = models.TextField(max_length=3000, null=True, blank=True)
    description_mn = models.TextField(max_length=3000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
