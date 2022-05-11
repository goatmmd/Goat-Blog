from django import forms

from articles.models import Post, Comment


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author', 'likes')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),

        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('user', 'post',)
