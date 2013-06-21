from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import FormView, UpdateView

from registration import signals
from registration.backends.default.views import RegistrationView
from registration.models import RegistrationProfile

from mesh.forms import ProfileForm, ProjectForm, UserRegistrationForm, EdgeForm, NodeForm
from mesh.models import Project, Edge, Node


class EditDataView(TemplateView):
    """

    """
    template_name = 'edit_data.html'

    def get_context_data(self, **kwargs):
        context = super(EditDataView, self).get_context_data(**kwargs)
        project = Project.objects.get(id=self.kwargs['project_id'])
        user = self.request.user

        if user != project.owner and user not in project.collaborators:
            raise PermissionDenied('Not authorised to edit this project!')

        context['project'] = project
        context['nodes'] = Node.objects.filter(project=project)
        context['edges'] = Edge.objects.filter(project=project)

        return context


class NodeCreateView(CreateView):
    """
    Create a new Node.

    """
    model = Node
    template_name = 'edit_data.html'

    def get_context_data(self, **kwargs):
        context = super(NodeCreateView, self).get_context_data(**kwargs)
        project = Project.objects.get(id=self.kwargs['project_id'])
        user = self.request.user

        if user != project.owner and user not in project.collaborators:
            raise PermissionDenied('Not authorised to edit this project!')

        context['project'] = project
        context['nodes'] = Node.objects.filter(project=project)
        context['edges'] = Edge.objects.filter(project=project)

        return context

    def get_success_url(self):
        return reverse_lazy('edit_data', kwargs=self.kwargs)


class EdgeCreateView(CreateView):
    """
    Create a new Edge.

    """
    form_class = EdgeForm
    model = Edge
    template_name = 'edit_data.html'

    def get_context_data(self, **kwargs):
        context = super(EdgeCreateView, self).get_context_data(**kwargs)
        project = Project.objects.get(id=self.kwargs['project_id'])
        user = self.request.user

        if user != project.owner and user not in project.collaborators:
            raise PermissionDenied('Not authorised to edit this project!')

        context['project'] = project
        context['nodes'] = Node.objects.filter(project=project)
        context['edges'] = Edge.objects.filter(project=project)

        return context

    def get_success_url(self):
        return reverse_lazy('edit_data', kwargs=self.kwargs)


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


class ProjectCreateView(FormView):
    """
    Create a new project.

    """
    form_class = ProjectForm
    template_name = 'project.html'

    def get_form_kwargs(self):
        kwargs = super(ProjectCreateView, self).get_form_kwargs()
        kwargs.update({'user' : self.request.user })
        return kwargs

    def form_valid(self, form):

        project = Project()
        project.owner = self.request.user

        data = form.cleaned_data
        project.name=data['name']
        project.description=data['description']
        project.node_description = data['node_description']
        project.edge_description = data['edge_description']
        project.save()
        project.collaborators.clear()
        for user in data['collaborators']:
            project.collaborators.add(user)
        project.save()
        project.collaborators = data['collaborators']

        messages.info(self.request, 'New project {} created'.format(project.name))
        return redirect('home')


class ProjectUpdateView(FormView):
    """
    Update existing project.

    """
    form_class = ProjectForm
    template_name = 'project.html'

    def get(self, request, project_id):
        project = Project.objects.get(id=project_id)
        form = ProjectForm(request.user, instance=project)
        return render(request, self.template_name, {'form' : form, 'project' : project})

    def get_form_kwargs(self):
        kwargs = super(ProjectUpdateView, self).get_form_kwargs()
        kwargs.update({'user' : self.request.user })
        return kwargs

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
            project.collaborators.clear()
            for user in data['collaborators']:
                project.collaborators.add(user)
            project.save()
            project.collaborators = data['collaborators']
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