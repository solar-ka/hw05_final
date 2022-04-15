from django import forms

from .models import Comment, Group, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group', 'image')

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('title', 'slug', 'description')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
