from django.forms import ModelForm
from .models import OtherAuthor
from django import forms


class OtherAuthorForm(ModelForm):
    class Meta:
        model = OtherAuthor
        fields = ['lastname', 'initials']


class OtherAuthorLeaderForm(ModelForm):
    class Meta:
        model = OtherAuthor
        fields = '__all__'


