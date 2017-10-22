from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.sites.models import Site
from django.views.generic import TemplateView, RedirectView
from django.contrib import admin

import views

urlpatterns = patterns('',
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^patrocinadores/$', views.PatrocinadoresView.as_view(), name='patrocinadores'),
    url(r'^competiciones/$', views.CompeticionesView.as_view(), name='competiciones'),
    url(r'^sobre_nosotros/', TemplateView.as_view(template_name='hokini/help/sobre_nosotros.html'), name='about'),
    url(r'^privacidad/', TemplateView.as_view(template_name='hokini/help/privacidad.html'), name='privacidad'),
    url(r'^condiciones/', TemplateView.as_view(template_name='hokini/help/condiciones.html'), name='condiciones'),
    url(r'^cookies/', TemplateView.as_view(template_name='hokini/help/cookies.html'), name='cookies'),
)