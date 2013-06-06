"""from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class MeshUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()

class MeshUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()

class MeshUserAdmin(UserAdmin):
    form = MeshUserChangeForm
    add_form = MeshUserCreationForm

admin.site.register(MeshUser, MeshUserAdmin)"""