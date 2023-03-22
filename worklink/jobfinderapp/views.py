from django.shortcuts import render
from django.views.generic import ListView
from companyapp import models as companyapp_models


class JobListingView(ListView):
    model = companyapp_models.Vacancy
    paginate = 5

    def get_queryset(self):
        return super().get_queryset().filter(is_closed=False)
    
    def get_context_data(self, **kwargs):
        companies = {el['id']: el['name'] for el in companyapp_models.Company.objects.values()}
        context = super().get_context_data(**kwargs)
        context['companies'] =  companies
        return context
    
    
