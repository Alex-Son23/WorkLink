from django.shortcuts import render


def index(request):
    content = {
        'title': 'Главная',
    }
    return render(request, 'index.html', context=content)
