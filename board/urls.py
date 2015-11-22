from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required, permission_required

from . import views

urlpatterns = patterns('',
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^list', views.TranslatorRequestList.as_view(), name="request_list"),
    url(r'^choose', views.ChooseLanguage.as_view(), name="choose_language"),
    url(r'^create', views.TranslatorRequestCreate.as_view(), name="request_create"),
)