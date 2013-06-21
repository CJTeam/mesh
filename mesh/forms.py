from django.contrib.auth.models import User
from django import forms
from registration.forms import RegistrationForm

from models import Project


class EditDataForm(forms.Form):
    pass


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name', 'description', 'node_description', 'edge_description']
        widgets = {
            'description': forms.Textarea(attrs={'': ''}),
        }

    class CollaboratorsField(forms.ModelMultipleChoiceField):
        def label_from_instance(self, user):
            return '{} {}'.format(user.first_name, user.last_name)

    def __init__(self, user, *args, **kwargs):

        if 'instance' in kwargs:
            initial = kwargs.setdefault('initial', {})
            initial['collaborators'] = [t.pk for t in kwargs['instance'].collaborators.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)

        self.fields['collaborators'] = ProjectForm.CollaboratorsField(required=False,queryset=User.objects.exclude(username=user.username).exclude(is_superuser=True))


class UserRegistrationForm(RegistrationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = [
            'first_name', 'last_name',
            'username', 'email',
            'password1', 'password2'
        ]