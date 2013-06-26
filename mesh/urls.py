from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from mesh.views import *

from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',

    url(r'^$', HomeView.as_view(), name="home" ),

    url(r'^browse_projects/$', BrowseProjectsView.as_view(), name='browse_projects'),
    url(r'^project/$', ProjectCreateView.as_view(), name='project_create'),
    url(r'^project/(?P<project_id>.*)/node_table/$', login_required(NodeTableView.as_view()), name='node_table'),
    url(r'^project/(?P<project_id>.*)/edge_table/$', login_required(EdgeTableView.as_view()), name='edge_table'),
    url(r'^project/(?P<project_id>.*)/edit_data/$', login_required(EditDataView.as_view()), name='edit_data'),
    url(r'^project/(?P<project_id>.*)/node/create$', login_required(NodeCreateView.as_view()), name='node_create'),
    url(r'^project/(?P<project_id>.*)/edge/create$', login_required(EdgeCreateView.as_view()), name='edge_create'),
    url(r'^project/(?P<project_id>.*)/collaborators/$', ProjectCollaboratorsView.as_view(), name='project_collaborators'),
    url(r'^project/(?P<project_id>.*)/csv/$', ProjectCsvView.as_view(), name='project_csv'),
    url(r'^project/(?P<project_id>.*)/deactivate/$', DeactivateProjectView.as_view(), name='deactivate_project'),
    url(r'^project/(?P<project_id>.*)/join/$', JoinProjectView.as_view(), name='join_project'),
    url(r'^project/(?P<project_id>.*)/gexf/$', ProjectGexfView.as_view(), name='project_gexf'),
    url(r'^project/(?P<project_id>.*)/graph/$', ProjectGraphView.as_view(), name='project_graph'),
    url(r'^project/(?P<project_id>.*)/$', ProjectUpdateView.as_view(), name='project_update'),

    # Registration
    url(r'^accounts/profile/$', ProfileView.as_view(), name='profile'),
    url(r'^accounts/register/$', RegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.default.urls')),

    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='auth_login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logout.html'}, name='auth_logout'),

    url(r'^admin/', include(admin.site.urls)),
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views' , {'document_root': settings.STATIC_ROOT}),
    )
