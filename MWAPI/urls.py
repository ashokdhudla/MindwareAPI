from django.conf.urls import patterns, include, url
from django.contrib import admin
from product.views import *
from rest_framework import routers
from news.views import *
from jobs.views import *
from quiz.views import *
from promotions.views import *
from survey.views import *
from mindwareuser.views import *

router = routers.DefaultRouter()

# user URLS
router.register(r'role',roleViewSet)
router.register(r'user',userViewSet)

# product Application  URLS
router.register(r'product',productViewSet)
router.register(r'pcategories',product_categoriesViewSet)
router.register(r'brand',brandViewSet)

# News Applications URLS
router.register(r'news',newsViewSet)
router.register(r'ncategories',news_categoriesViewSet)

# Job Application URLS
router.register(r'jobs',jobViewSet)
router.register(r'japplications',job_applicationViewSet)
router.register(r'jdepartment',job_departmentViewSet)

# Quiz URLS
router.register(r'quiz',quizViewSet)

# Promotions URLS
router.register(r'promotion',promotionsViewSet)

# Survey URLS

router.register(r'survey',promotionsViewSet)
router.register(r'soptions', survey_optionsViewSet)
router.register(r'squestions', survey_questionsViewSet)
router.register(r'sresponse',survey_responseViewSet)




urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^mindware/api/',include(router.urls)),
)
