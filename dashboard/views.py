from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class landing_page_view(TemplateView):
    template_name = "index.html"