from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from mesh.views import HomeView, ProfileView, ProjectCreateView, ProjectUpdateView, RegistrationView

from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',

    url(r'^$', HomeView.as_view(), name="home" ),

    url(r'^project/$', ProjectCreateView.as_view(), name='project_create'),
    url(r'^project/(?P<project_id>.*)/$', ProjectUpdateView.as_view(), name='project_update'),

    # Registration
    url(r'^accounts/profile/$', ProfileView.as_view(), name='profile'),
    url(r'^accounts/register/$', RegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.default.urls')),

    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='auth_login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logout.html'}, name='auth_logout'),

    url(r'^admin/', include(admin.site.urls)),
)
