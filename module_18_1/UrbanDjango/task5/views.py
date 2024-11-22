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
            #print('Пользователь уже есть в списке!')
            info.update({'error': username})
        elif password != repeat_password:
            #print('Пароли не совпадают!')
            info.update({'error':password})
        elif int(age) < 18:
            #print('Возраст < 18')
            info.update({'error': age})
        else:
            #print('Годится!')
            return HttpResponse('Приветствуем, %s!' % username)

    #print(info)
    return render(request, 'registration_page.html', info)



# def index6(request):
#     if request.method == 'POST':
#         # Получаем данные:
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         subscribe = request.POST.get('subscribe') == 'on'
#
#         print(f'Name: {name}')
#         print(f'Email: {email}')
#         print(f'Message: {message}')
#         print(f'Subscribe: {subscribe}')
#
#         # Ответ пользователю:
#         return HttpResponse('Форма успешно отправлена!')
#     # Если это GET
#     return render(request, 'index6.html')