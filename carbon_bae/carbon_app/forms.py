from django.forms import ModelForm
from django import forms
from .models import User,PostImage

class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['bio','image_url']

form = UserForm()

class ImageForm(ModelForm):

    class Meta:
        model = PostImage
        fields = ['image_url']

form = ImageForm()
