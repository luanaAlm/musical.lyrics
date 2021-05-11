from django.forms import ModelForm
from .models import Songs


class SongsForm(ModelForm):
    class Meta:
        model = Songs
        fields = "__all__"
