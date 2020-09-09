from django import forms

from .models import Post


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(required=True)
    content = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['title', 'content', 'image']