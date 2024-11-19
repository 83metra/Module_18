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
    text = 'Здесь можно купить старые добрые игры. Неувядающая классика, заставляющая Вас рыдать от ностальгического восторга!'
    first = 'Doom II'
    second = 'Warcraft II'
    third = 'Vikings'
    context = {
        'title': title,
        'text': text,
        'first': first,
        'second': second,
        'third': third
    }
    return render(request, 'verkaufhaus.html', context)

def korb(request):
    title = 'Корзина'
    text = 'Корзина пуста'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'korb.html', context)

