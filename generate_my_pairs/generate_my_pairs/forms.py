from django import forms
from generate_my_pairs.models import Post
from django.forms import extras
from django.contrib.admin.widgets import AdminDateWidget


class UploadFileForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    file = forms.FileField()

    class Meta:
        model = Post
        fields = [
            'title',
            'file',
        ]
