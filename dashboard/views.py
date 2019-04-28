from django.shortcuts import render
from django.views.generic import TemplateView
from dashboard.models import Problem_statements
from dashboard.models import learn_statements
# Create your views here.

class landing_page_view(TemplateView):
    template_name = "index.html"

def problem_page(request):
    problems = Problem_statements.objects.all()
    return render(request, 'problem.html', { 'problems': problems })

def dashboard_page(request):
    return render(request, 'dashboard.html', {})

def solve_page(request):
    return render(request, 'solve.html', {})

def learn_page(request):
    learns = learn_statements.objects.all()
    return render(request, 'learn.html', { 'learns': learns }) 