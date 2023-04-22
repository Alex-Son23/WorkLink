from django.shortcuts import render
from mainapp.models import Vacancy
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.is_superuser)
def vacancies(request):
    title = 'Админка/вакансии'

    vacancies_list = Vacancy.objects.filter(visible=False)

    content = {
        'title': title,
        'objects': vacancies_list
    }

    return render(request, 'adminapp/vacancies.html', content)


@user_passes_test(lambda u: u.is_superuser)
def vacancies_plus(request, pk):

    vacancies_visible = Vacancy.objects.get(pk=pk)
    vacancies_visible.visible = True
    vacancies_visible.save()

    title = 'Админка/вакансии'
    vacancies_list = Vacancy.objects.filter(visible=True)

    content = {
        'title': title,
        'objects': vacancies_list
    }

    return render(request, 'adminapp/vacancies_plus.html', content)
