from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def index(request):
    return render(request, 'calculators/index.html')

class DynamicCleansFeesView(TemplateView):
    template_name = 'index.html'
