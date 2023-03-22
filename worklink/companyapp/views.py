from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView
from companyapp import models as companyapp_models
from authapp.models import CompanyProfile


class VacancyView(ListView):
    model = companyapp_models.Vacancy
    # paginate = 5

    def get_queryset(self):
        return super().get_queryset().filter(is_closed=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вакансии'
        return context


def vacancy(request, pk):
    title = 'детали продукта'
    # links_menu = companyapp_models.Vacancy.objects.all()
    vacancy = get_object_or_404(companyapp_models.Vacancy, pk=pk)

    context = {
        'title': title,
        'vacancy': vacancy,
    }

    return render(request, 'companyapp/vacancy.html', context=context)


def company(request, pk):
    title = 'Компания'
    # links_menu = companyapp_models.Vacancy.objects.all()
    company = get_object_or_404(CompanyProfile, pk=pk)

    context = {
        'title': title,
        'company': company,
    }

    return render(request, 'companyapp/company.html', context=context)
