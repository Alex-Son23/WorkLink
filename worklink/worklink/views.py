from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from authapp.forms import JobForm
from authapp.models import JobList
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, HttpResponseRedirect


class IndexView(TemplateView):
    template_name = 'worklink/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'WorkLink'
        return context


class NewsView(TemplateView):
    template_name = 'worklink/news.html'


class ContactsView(TemplateView):
    template_name = 'worklink/contacts.html'


# Список вакансий на странице работодателя
# class JobListView(TemplateView):
#     template_name = 'worklink/job_list.html'
#
#     def get_context_data(self, **kwargs):
#         context_data = super().get_context_data(**kwargs)
#         context_data['object_list'] = JobList.objects.all()
#         return context_data

class JobListView(ListView):
    template_name = 'worklink/job_list.html'
    model = JobList
    paginate_by = 3

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class JobDetailView(DetailView):
    template_name = 'worklink/job_detail.html'
    model = JobList


class JobFormView(CreateView):
    template_name = 'worklink/job_form.html'
    model = JobList
    form_class = JobForm
    success_url = '/job_form/?ADDED=Y'
    # success_url = reverse_lazy('job_form')

    def get_context_data(self, **kwargs):
        context = super(JobFormView, self).get_context_data(**kwargs)

        if self.request.method == 'POST':
            new_form = JobForm(self.request.POST)

            if new_form.is_valid():
                result = new_form.save()

                return HttpResponseRedirect(reverse_lazy('job_form') + '?ADDED=Y')

        context['success'] = self.request.GET.get('ADDED') == 'Y'
        return context