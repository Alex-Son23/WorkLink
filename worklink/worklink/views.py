from django.views.generic import TemplateView
from authapp.models import JobFinderProfile
from mainapp.models import Resume

class IndexView(TemplateView):
    template_name = 'worklink/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['new_candidates'] = JobFinderProfile.objects.all()[:6]
        context['title'] = 'WorkLink'
        return context


class NewsView(TemplateView):
    template_name = 'worklink/news.html'


class ContactsView(TemplateView):
    template_name = 'worklink/contacts.html'


# Список вакансий на странице работодателя
# class JobListView(TemplateView):
#     template_name = 'worklink/vacancies.html'
#
#     def get_context_data(self, **kwargs):
#         context_data = super().get_context_data(**kwargs)
#         context_data['object_list'] = JobList.objects.all()
#         return context_data
