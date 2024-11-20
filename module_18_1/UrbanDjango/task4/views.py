from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def platform(request):
    title = 'Магазин ретро-игр'
    text = 'Главная страница'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'platform.html', context)

def shop(request):
    title = 'Магазин'
    text = 'Магазин'
    context = {
        'title': title,
        'text': text,
        'games:': ['Doom II', 'Warcraft', 'Vikings'],
    }
    return render(request, 'shop.html', context)

def cart(request):
    title = 'Корзина'
    text = 'Корзина пуста'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'cart.html', context)


