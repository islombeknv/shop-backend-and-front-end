from .models import CommentModel
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('name', 'email', 'comment', 'phone')