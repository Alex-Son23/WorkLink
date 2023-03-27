from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from companyapp.forms import JobForm
from companyapp.models import JobList


class JobListView(ListView):
    template_name = 'companyapp/vacancies.html'
    model = JobList
    paginate_by = 3

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

    def get_context_data(self, **kwargs):
        context = super(JobListView, self).get_context_data(**kwargs)
        context['title'] = 'Вакансии компании'

        return context


class JobDetailView(DetailView):
    template_name = 'companyapp/vacancy_detail.html'
    model = JobList

    def get_context_data(self, **kwargs):
        context = super(JobDetailView, self).get_context_data(**kwargs)
        context['title'] = self.object.title

        return context


class JobFormView(CreateView):
    template_name = 'companyapp/vacancy_add.html'
    model = JobList
    form_class = JobForm
    success_url = '/vacancies/add/?ADDED=Y'

    def get_context_data(self, **kwargs):
        context = super(JobFormView, self).get_context_data(**kwargs)
        context['title'] = 'Добавление вакансии'

        if self.request.method == 'POST':
            new_form = JobForm(self.request.POST)

            if new_form.is_valid():
                result = new_form.save()

                return HttpResponseRedirect(reverse_lazy('vacancy_add') + '?ADDED=Y')

        context['success'] = self.request.GET.get('ADDED') == 'Y'
        return context


class JobUpdateView(UpdateView):
    template_name = 'companyapp/vacancy_edit.html'
    model = JobList
    form_class = JobForm

    def get_success_url(self):
        return reverse_lazy('vacancy_edit',
                            kwargs={'pk': self.object.pk}) + '?SAVED=Y'

    def get_context_data(self, **kwargs):
        context = super(JobUpdateView, self).get_context_data(**kwargs)
        context['title'] = self.object.title

        if self.request.method == 'POST':
            new_form = JobForm(self.request.POST)

            if new_form.is_valid():
                result = new_form.save()

                return HttpResponseRedirect(reverse_lazy('vacancy_edit',
                                             kwargs={'pk': self.object.pk}) + '?SAVED=Y')

        context['success'] = self.request.GET.get('SAVED') == 'Y'
        return context
