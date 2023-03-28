
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from companyapp.forms import VacancyForm
from companyapp.models import Vacancy


from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView
from companyapp import models as companyapp_models
from authapp.models import CompanyProfile
# from companyapp.forms import ResponseForm


class VacancyListView(ListView):
    template_name = 'companyapp/vacancies.html'
    model = Vacancy
    paginate_by = 3
    ordering = ['-created_at']

    def get_queryset(self):
        return super().get_queryset().filter(is_closed=False,
                                             company_id=self.request.user.get_company())

    def get_context_data(self, **kwargs):
        context = super(VacancyListView, self).get_context_data(**kwargs)
        context['title'] = 'Вакансии компании'

        return context


# Контроллер детальное описание вакансии
class VacancyDetailView(DetailView):
    template_name = 'companyapp/vacancy_detail.html'
    model = Vacancy

    def get_context_data(self, **kwargs):
        context = super(VacancyDetailView, self).get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


# Контроллер добавления вакансии
class VacancyCreateView(CreateView):
    template_name = 'companyapp/vacancy_form.html'
    model = Vacancy
    form_class = VacancyForm

    def get_success_url(self):
        return reverse_lazy('company:vacancy_add') + '?ADDED=Y'

    def form_valid(self, form):
        form.instance.company_id = self.request.user.get_company()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(VacancyCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Добавление вакансии'
        context['success_message'] = 'Вакансия добавлена'
        context['submit_title'] = 'Добавить'
        context['form_action'] = reverse_lazy('company:vacancy_add')
        context['success'] = self.request.GET.get('ADDED') == 'Y'
        return context


class VacancyUpdateView(UpdateView):
    template_name = 'companyapp/vacancy_form.html'
    model = Vacancy
    form_class = VacancyForm

    def form_valid(self, form):
        form.instance.company_id = self.request.user.get_company()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('company:vacancy_edit',
                            kwargs={'pk': self.object.pk}) + '?SAVED=Y'

    def get_context_data(self, **kwargs):
        context = super(VacancyUpdateView, self).get_context_data(**kwargs)
        context['title'] = self.object.title
        context['success_message'] = 'Изменения сохранены'
        context['submit_title'] = 'Сохранить'
        context['form_action'] = reverse_lazy('company:vacancy_edit', kwargs={'pk': self.object.pk})
        context['success'] = self.request.GET.get('SAVED') == 'Y'
        return context
=======


class VacancyView(ListView):
    model = companyapp_models.Vacancy

    paginate_by = 3

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


# def respond_to_vacancy(request, pk):
#     vacancy = get_object_or_404(companyapp_models.Vacancy, pk=pk)
#     if request.method == 'POST':
#         form = ResponseForm(request.POST)
#         if form.is_valid():
#             return render(request, 'companyapp/response_success.html')
#     else:
#         form = ResponseForm()
#     return render(request, 'companyapp/respond_to_vacancy.html', {'form': form, 'vacancy': vacancy})

