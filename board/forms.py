from django import forms


class ThreadPostForm(forms.Form):
    author = forms.CharField(initial="Аноним")
    content = forms.CharField(widget=forms.Textarea())
    picture_url = forms.URLField(required=None)
