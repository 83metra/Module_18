from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def welcome(request):
    return render(request, 'func_template.html')

class Welcome(TemplateView):
    template_name = ('class_template.html')