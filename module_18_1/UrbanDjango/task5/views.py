from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .forms import UserRegister

def sign_up_by_django(request):
    users = ['Otto', 'Moritz', 'Ruslan', 'Finduss', 'Karl']
    info = {}
    if request.method == 'post':
        form = UserRegister()
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']


    else:
        form = UserRegister()
    print(form.get_context)
    return render(request, 'registration_page.html', {'form': form})


def sign_up_by_html(request):
    users = ['Otto', 'Moritz', 'Ruslan', 'Finduss', 'Karl']
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')


        if username in users:
            info.update({'error': 'Пользователь уже существует.'})
        elif password != repeat_password:
            info.update({'error': 'Пароли не совпадают.'})
        elif int(age) < 18:
            info.update({'error': 'Вы должны быть старше 18.'})
        else:
            return HttpResponse('Приветствуем, %s!' % username)

    #print(info)
    return render(request, 'registration_page.html', info)