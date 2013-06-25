import json

from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView, CreateView, View
from django.core.mail import send_mail
from django.views.generic.edit import FormView, UpdateView

from registration import signals
from registration.backends.default.views import RegistrationView
from registration.models import RegistrationProfile

from mesh.forms import ProfileForm, ProjectForm, UserRegistrationForm, EdgeForm, NodeForm
from mesh.models import Project, Edge, Node
from mesh import util


class BrowseProjectsView(TemplateView):
    """
    List all Projects.

    """
    template_name = 'browse_projects.html'

    def get_context_data(self, **kwargs):
        context = super(BrowseProjectsView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all().order_by('name')
        return context


class DeactivateProjectView(View):
    """
    Deactivate (delete) a project.

    """
    def post(self, request, project_id):
        project = Project.objects.get(id=project_id)
        if project.owner != request.user:
            raise PermissionDenied()
        project.delete()
        messages.info(self.request, 'Project {} deactivated'.format(project.name))
        return redirect('home')


class EditDataView(TemplateView):
    """

    """
    template_name = 'edit_data.html'

    def get_context_data(self, **kwargs):
        context = super(EditDataView, self).get_context_data(**kwargs)
        project = Project.objects.get(id=self.kwargs['project_id'])
        user = self.request.user

        if user != project.owner and user not in project.collaborators.all():
            raise PermissionDenied('Not authorised to edit this project!')

        context['project'] = project
        context['nodes'] = Node.objects.filter(project=project)
        context['edges'] = Edge.objects.filter(project=project)

        return context


class NodeCreateView(CreateView):
    """
    Create a new Node via AJAX request.

    """
    model = Node
    template_name = 'edit_data.html'

    def form_invalid(self, form):
        return HttpResponseBadRequest(json.dumps({'errors' : form.errors.keys()}))

    def get_context_data(self, **kwargs):
        user = self.request.user
        if user != project.owner and user not in project.collaborators:
            raise PermissionDenied('Not authorised to edit this project!')
        return super(NodeCreateView, self).get_context_data(**kwargs)

    def get_success_url(self):
        return reverse_lazy('node_table', kwargs=self.kwargs)


class NodeTableView(TemplateView):
    """
    HTML fragment for project node table.

    """
    template_name = 'node_table.html'

    def get_context_data(self, **kwargs):
        context = super(NodeTableView, self).get_context_data(**kwargs)
        project = Project.objects.get(id=kwargs['project_id'])
        context['nodes'] = Node.objects.filter(project=project)
        return context


class EdgeCreateView(CreateView):
    """
    Create a new Edge.

    """
    model = Edge
    template_name = 'edit_data.html'

    def form_invalid(self, form):
        return HttpResponseBadRequest(json.dumps({'errors' : form.errors.keys()}))

    def get_context_data(self, **kwargs):
        user = self.request.user
        if user != project.owner and user not in project.collaborators:
            raise PermissionDenied('Not authorised to edit this project!')
        return super(EdgeCreateView, self).get_context_data(**kwargs)

    def get_success_url(self):
        return reverse_lazy('edge_table', kwargs=self.kwargs)


class EdgeTableView(TemplateView):
    """
    HTML fragment for project edge table.

    """
    template_name = 'edge_table.html'

    def get_context_data(self, **kwargs):
        context = super(EdgeTableView, self).get_context_data(**kwargs)
        project = Project.objects.get(id=kwargs['project_id'])
        context['edges'] = Edge.objects.filter(project=project)
        return context


class HomeView(TemplateView):
    """
    Home view displays projects when logged in.

    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        if self.request.user.is_authenticated():
            context['owner_projects'] = self.request.user.project_set
            context['collaborator_projects'] = self.request.user.collaborator_projects

        return context


class JoinProjectView(View):
    """
    Contact project and request access to project.

    """
    def post(self, request, project_id):
        project = Project.objects.get(id=project_id)
        send_mail('Mesh Project Access Request',
                  '{} {} with email address {} is requesting access to the project {}.'.format(request.user.first_name,
                                                                                               request.user.last_name,
                                                                                               request.user.email,
                                                                                               project.name),
                  'projects@mesh.com',
                  [project.owner.email],
                  fail_silently=False)
        messages.info(self.request, 'Request for access to project {} sent'.format(project.name))
        return redirect('home')


class ProfileView(UpdateView):
    """
    View/update user profile.

    """
    form_class = ProfileForm
    model = User
    template_name = 'registration/profile.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        messages.info(self.request, 'Profile updated')
        return reverse('home')


class ProjectCollaboratorsView(TemplateView):
    """
    View and update collaborators for a project.

    """
    template_name = 'collaborators.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectCollaboratorsView, self).get_context_data(**kwargs)
        context['project'] = project = Project.objects.get(id=kwargs['project_id'])
        context['users'] = User.objects.filter(is_superuser=False).filter(is_active=True).exclude(id=project.owner.id)
        return context

    def post(self, request, project_id):
        # Update collaborators list
        project = Project.objects.get(id=project_id)
        project.collaborators.clear()
        for user_id in request.POST.getlist('collaborators'):
            user = User.objects.get(id=user_id)
            project.collaborators.add(user)
        project.save()
        messages.info(self.request, 'Collaborators for project {} updated'.format(project.name))
        return redirect('project_update', project_id)


class ProjectCreateView(FormView):
    """
    Create a new project.

    """
    form_class = ProjectForm
    template_name = 'project.html'

    def form_valid(self, form):

        project = Project()
        project.owner = self.request.user

        data = form.cleaned_data
        project.name=data['name']
        project.description=data['description']
        project.node_description = data['node_description']
        project.edge_description = data['edge_description']
        project.save()

        messages.info(self.request, 'New project {} created'.format(project.name))
        return redirect('project_update', project_id=project.id)


class ProjectCsvView(View):
    def get(self, request, project_id):
        project = Project.objects.get(id=project_id)
        response = HttpResponse(mimetype='text/csv')
        response['Content-Disposition'] = "attachment; filename={}.csv".format(project.name)
        util.write_gephi_csv(response, project)
        return response


class ProjectGexfView(View):
    def get(self, request, project_id):
        project = Project.objects.get(id=project_id)
        response = HttpResponse(mimetype='text/xml')
        response['Content-Disposition'] = "attachment; filename={}.gexf".format(project.name)
        util.write_gexf(response, project)
        return response


class ProjectGraphView(TemplateView):
    template_name = 'project_graph.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectGraphView, self).get_context_data(**kwargs)
        context['project'] = project = Project.objects.get(id=kwargs['project_id'])
        context['graph_json'] = util.project_graph_json(project)
        return context


class ProjectUpdateView(FormView):
    """
    Update existing project.

    """
    form_class = ProjectForm
    template_name = 'project.html'

    def get(self, request, project_id):
        project = Project.objects.get(id=project_id)
        form = ProjectForm(instance=project)
        return render(request, self.template_name, {'form' : form, 'project' : project})

    def post(self, request, project_id):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            project = Project.objects.get(id=project_id)
            if project.owner <> self.request.user:
                raise PermissionDenied()
            data = form.cleaned_data
            project.name=data['name']
            project.description=data['description']
            project.node_description = data['node_description']
            project.edge_description = data['edge_description']
            project.save()
            messages.info(self.request, 'Project {} updated'.format(project.name))
            return redirect('home')
        else:
            return self.form_invalid(form)


class RegistrationView(RegistrationView):
    """
    Custom registration view.

    """
    form_class = UserRegistrationForm
    def register(self, request, **cleaned_data):
        """
        Override django-registration register method to save extra fields on User.

        """
        first_name, last_name, username, email, password = cleaned_data['first_name'], cleaned_data['last_name'], cleaned_data['username'], cleaned_data['email'], cleaned_data['password1']
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)
        new_user = RegistrationProfile.objects.create_inactive_user(username, email,
                                                                    password, site)

        # Set extra fields
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()

        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        return new_user
