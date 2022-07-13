from dataclasses import fields
from .models import Post, Comments
from django import forms

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["slug", "author"]
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["name", "comment"]