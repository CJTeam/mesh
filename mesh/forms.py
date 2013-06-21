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