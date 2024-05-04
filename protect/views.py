from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'
