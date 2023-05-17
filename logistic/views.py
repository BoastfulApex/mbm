from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *


class SliderList(ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer 


class NewsList(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer 


class CommentList(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer 


class FAQList(ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer 


class ServiceList(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer 


class ServiceCategoryList(ModelViewSet):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer 


class PartnerList(ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer 

