from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from authapp.models import CompanyProfile
from companyapp.forms import VacancyForm
from companyapp.models import Vacancy


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


class VacancyDetailView(DetailView):
    template_name = 'companyapp/vacancy_detail.html'
    model = Vacancy

    def get_context_data(self, **kwargs):
        self.request.user.get_company()
        context = super(VacancyDetailView, self).get_context_data(**kwargs)
        context['title'] = self.object.title

        return context


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
