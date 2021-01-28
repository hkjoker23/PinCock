from profileapp.models import Profile
from django.forms.models import ModelForm


class ProfileCreationForm(ModelForm):
    class Meta:
        modle = Profile
        fields = ['image','nickname','message']