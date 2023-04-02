from django.db.models import F
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from jobfinderapp.forms import ResumeForm
from jobfinderapp.models import Experience, Resume


class ResumeListView(ListView):
    template_name = 'jobfinderapp/resume_list.html'
    model = Resume
    paginate_by = 10
    ordering = ['id']

    def get_queryset(self):
        return super().get_queryset().filter(user_id=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ResumeListView, self).get_context_data(**kwargs)
        context['title'] = 'Мои резюме'

        return context
    

# Контроллер добавления вакансии*
class ResumeCreateView(CreateView):
    template_name = 'jobfinderapp/resume_form.html'
    model = Resume
    form_class = ResumeForm

    def get_success_url(self):
        return reverse_lazy('jobfinder:resume_add') + '?ADDED=Y'

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ResumeCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Добавление резюме'
        context['success_message'] = 'Резюме добавлена'
        context['submit_title'] = 'Добавить'
        context['form_action'] = reverse_lazy('jobfinder:resume_add')
        context['success'] = self.request.GET.get('ADDED') == 'Y'
        return context


class ResumeUpdateView(UpdateView):
    template_name = 'jobfinderapp/resume_form.html'
    model = Resume
    form_class = ResumeForm

    def form_valid(self, form):
        form.instance.company_id = self.request.user.get_company()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('jobfinder:resume_edit',
                            kwargs={'pk': self.object.pk}) + '?SAVED=Y'

    def get_context_data(self, **kwargs):
        context = super(ResumeUpdateView, self).get_context_data(**kwargs)
        context['title'] = self.object.title
        context['success_message'] = 'Изменения сохранены'
        context['submit_title'] = 'Сохранить'
        context['form_action'] = reverse_lazy('jobfinder:resume_edit', kwargs={'pk': self.object.pk})
        context['success'] = self.request.GET.get('SAVED') == 'Y'
        return context