from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def hauptseite(request):
    title = 'Магазин ретро-игр'
    text = 'Главная страница'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'hauptseite.html', context)

def verkaufhaus(request):
    title = 'Магазин'
    text = 'Здесь можно купить старые добрые игры.'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'verkaufhaus.html', context)

