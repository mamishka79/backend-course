from django import forms


class BlogCreationForm(forms.Form):
    title = forms.CharField(min_length=5, max_length=200, required=True)
    description = forms.CharField(min_length=5, max_length=200, required=True)
    author = forms.CharField(min_length=5, max_length=200, required=True)
