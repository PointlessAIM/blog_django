from django import forms
from .models import Post

class BlogForm(forms.Form):
    name = forms.CharField(label="Enter blog name",max_length=100)
    tagline = forms.CharField(widget=forms.Textarea)
class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"