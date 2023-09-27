from django import forms


class BlogForm(forms.Form):
    author_name = forms.CharField()
    title = forms.CharField()
    text = forms.SlugField()
