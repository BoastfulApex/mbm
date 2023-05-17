from rest_framework import routers
from logistic.views import *

router = routers.DefaultRouter()

router.register("sliders", SliderList, basename="sliders")
router.register("comments", CommentList, basename="comments")
router.register("faq", FAQList, basename="faq")
router.register("news", NewsList, basename="news")
router.register("services", ServiceList, basename="services")
router.register("services_category", ServiceCategoryList, basename="services_category")
router.register("partners", PartnerList, basename="partners")