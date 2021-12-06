from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import Textarea
from .models import Image,Comments, Profile

class CommentForm(forms.ModelForm):
    comment = forms.CharField(label='Leave a comment',max_length=30)

    class Meta:
        model = Comments
        fields = ('comment',)