from django.shortcuts import render
from django.views.generic import TemplateView
from authapp.forms import JobForm
from authapp.models import JobList


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
class JobListing(TemplateView):
    template_name = 'worklink/job_listing.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = JobList.objects.all()
        return context_data


