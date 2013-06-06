from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', TemplateView.as_view(template_name="index.html"), name="home" ),

    # Registration
    (r'^accounts/', include('registration.urls')),

    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='auth_login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logout.html'}, name='auth_logout'),

    url(r'^admin/', include(admin.site.urls)),
)
