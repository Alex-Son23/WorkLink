from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from companyapp.forms import VacancyForm
from companyapp.models import VacancyListModel


# Контроллер списка вакансий
class VacancyListView(ListView):
    template_name = 'companyapp/vacancies.html'
    model = VacancyListModel
    paginate_by = 3

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

    def get_context_data(self, **kwargs):
        context = super(VacancyListView, self).get_context_data(**kwargs)
        context['title'] = 'Вакансии компании'

        return context


# Контроллер детальное описание вакансии
class VacancyDetailView(DetailView):
    template_name = 'companyapp/vacancy_detail.html'
    model = VacancyListModel

    def get_context_data(self, **kwargs):
        context = super(VacancyDetailView, self).get_context_data(**kwargs)
        context['title'] = self.object.title

        return context


# Контроллер добавления вакансии
class VacancyFormView(CreateView):
    template_name = 'companyapp/vacancy_add.html'
    model = VacancyListModel
    form_class = VacancyForm
    success_url = '/vacancies/add/?ADDED=Y'

    def get_context_data(self, **kwargs):
        context = super(VacancyFormView, self).get_context_data(**kwargs)
        context['title'] = 'Добавление вакансии'

        if self.request.method == 'POST':
            new_form = VacancyForm(self.request.POST)

            if new_form.is_valid():
                result = new_form.save()

                return HttpResponseRedirect(reverse_lazy('vacancy_add') + '?ADDED=Y')

        context['success'] = self.request.GET.get('ADDED') == 'Y'
        return context


class VacancyUpdateView(UpdateView):
    template_name = 'companyapp/vacancy_edit.html'
    model = VacancyListModel
    form_class = VacancyForm

    def get_success_url(self):
        return reverse_lazy('vacancy_edit',
                            kwargs={'pk': self.object.pk}) + '?SAVED=Y'

    def get_context_data(self, **kwargs):
        context = super(VacancyUpdateView, self).get_context_data(**kwargs)
        context['title'] = self.object.title

        if self.request.method == 'POST':
            new_form = VacancyForm(self.request.POST)

            if new_form.is_valid():
                result = new_form.save()

                return HttpResponseRedirect(reverse_lazy('vacancy_edit',
                                             kwargs={'pk': self.object.pk}) + '?SAVED=Y')

        context['success'] = self.request.GET.get('SAVED') == 'Y'
        return context
