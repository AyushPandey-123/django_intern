from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView,CreateView
from .models import User,PostImage
from .forms import UserForm,ImageForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import TextInput
from django import forms
from django.views.generic.list import ListView
from django.urls import reverse_lazy
# Create your views here.

# class IndexView(TemplateView):
#     template_name = "index.html"

class ImageList(ListView):
    model = PostImage
    template_name = "postimage_list.html"


class AboutUser(TemplateView):
    template_name = "about_user.html"

class UserCreate(LoginRequiredMixin,UpdateView):
    model = User
    fields = ['bio', 'image_url']
    template_name = "user_form.html"
    success_url= reverse_lazy("about")

    def get_object(self, queryset=None):
        return self.request.user

class UploadImage(LoginRequiredMixin,CreateView):
    model = PostImage
    fields = ['image_url']
    template_name = "upload_image.html"
    success_url= "/"
