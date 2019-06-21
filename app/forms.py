from django import forms

from.models import Video, Theme


# forms

# + ------------------------------------------------------------------------- +
class VideoUploadForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ('file', 'name', 'theme')
# + ------------------------------------------------------------------------- +


# + ------------------------------------------------------------------------- +
class ThemeForm(forms.ModelForm):

    class Meta:
        model = Theme
        fields = ('name',)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        name_was_registered = Theme.objects.filter(name=name).first()

        if name_was_registered:
            raise forms.ValidationError("Ths theme exists!")
        
        return name
# + ------------------------------------------------------------------------- +
