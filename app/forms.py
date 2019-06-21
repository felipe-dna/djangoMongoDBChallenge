from django import forms

from.models import Video, Theme

# forms


class VideoUploadForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ('file', 'name', 'theme')