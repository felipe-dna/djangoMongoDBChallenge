from django import forms

from.models import Video, Theme

# forms


class VideoCreateForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ('file', 'name', 'theme')