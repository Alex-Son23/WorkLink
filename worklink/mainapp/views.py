from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from mainapp.forms import VacancyForm, ResponseForm, OfferForm, AddPostForm
from mainapp.models import Vacancy

from django.shortcuts import render, get_object_or_404

from mainapp import models as companyapp_models
from authapp.models import CompanyProfile, JobFinderProfile
from mainapp.forms import ResumeForm, ExperienceFormSet, ExperienceFormSetCreate, ApplyForm, OfferApplyForm
from mainapp.models import Experience, Resume, Response, Status, Offer


# Контроллер списка вакансий
class VacancyListView(ListView):
    template_name = 'mainapp/vacancies.html'
    model = Vacancy
    paginate_by = 5
    ordering = ['-created_at']

    def get_queryset(self):
        return super().get_queryset().filter(is_closed=False,
                                             company=self.request.user.get_company())

    def get_context_data(self, **kwargs):
        context = super(VacancyListView, self).get_context_data(**kwargs)
        context['title'] = 'Вакансии компании'

        return context


# Контроллер детальное описание вакансии
class VacancyDetailView(DetailView):
    template_name = 'mainapp/vacancy_detail.html'
    model = Vacancy

    def get_context_data(self, **kwargs):
        context = super(VacancyDetailView, self).get_context_data(**kwargs)
        context['title'] = self.object.title
        return context


# Контроллер добавления вакансии
class VacancyCreateView(CreateView):
    template_name = 'mainapp/vacancy_form.html'
    model = Vacancy
    form_class = VacancyForm

    def get_success_url(self):
        return reverse_lazy('company:vacancy_add') + '?ADDED=Y'

    def form_valid(self, form):
        form.instance.company = self.request.user.get_company()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(VacancyCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Добавление вакансии'
        context['success_message'] = 'Вакансия добавлена'
        context['submit_title'] = 'Добавить'
        context['form_action'] = reverse_lazy('company:vacancy_add')
        context['success'] = self.request.GET.get('ADDED') == 'Y'
        return context


# Контроллер редактирования вакансии
class VacancyUpdateView(UpdateView):
    template_name = 'mainapp/vacancy_form.html'
    model = Vacancy
    form_class = VacancyForm

    def form_valid(self, form):
        form.instance.company = self.request.user.get_company()
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


# Список вакансий
class VacancyView(ListView):
    model = companyapp_models.Vacancy

    paginate_by = 3

    def get_queryset(self):
        return super().get_queryset().filter(is_closed=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вакансии'
        return context


# Контроллер для откликов к вакансии
class VacancyResponsesListView(ListView):
    model = Response
    template_name = 'mainapp/vacancy_responses.html'

    def get_queryset(self):
        return super().get_queryset().filter(vacancy=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vacancy = get_object_or_404(Vacancy, pk=self.kwargs['pk'])
        context['title'] = f'Отклики на вакансию "{vacancy.title}"'
        return context


# Контроллер для предложений по вакансии
class VacancyOffersListView(ListView):
    model = Offer
    template_name = 'mainapp/vacancy_offers.html'

    def get_queryset(self):
        return super().get_queryset().filter(vacancy=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vacancy = get_object_or_404(Vacancy, pk=self.kwargs['pk'])
        context['title'] = f'Предложения по вакансии "{vacancy.title}"'
        return context


class VacancyResponseUpdateView(UpdateView):
    template_name = 'mainapp/vacancy_response_form.html'
    model = Response
    form_class = ResponseForm

    def get_success_url(self):
        return reverse_lazy('company:vacancy_response_update', kwargs={
            'vacancy_id': self.object.vacancy.pk,
            'pk': self.object.pk,
        }) + '?SAVED=Y'

    def get_context_data(self, **kwargs):
        context = super(VacancyResponseUpdateView, self).get_context_data(**kwargs)
        context['title'] = self.object.vacancy.title
        context['sub_title'] = 'Отклики'
        context['success_message'] = 'Изменения сохранены'
        context['submit_title'] = 'Сохранить'
        context['form_action'] = reverse_lazy('company:vacancy_response_update', kwargs={
            'vacancy_id': self.object.vacancy.pk,
            'pk': self.object.pk,
        })
        context['success'] = self.request.GET.get('SAVED') == 'Y'
        return context


class VacancyOfferUpdateView(UpdateView):
    template_name = 'mainapp/vacancy_offer_form.html'
    model = Offer
    form_class = OfferForm

    def get_success_url(self):
        return reverse_lazy('company:vacancy_offer_update', kwargs={
            'vacancy_id': self.object.vacancy.pk,
            'pk': self.object.pk,
        }) + '?SAVED=Y'

    def get_context_data(self, **kwargs):
        context = super(VacancyResponseUpdateView, self).get_context_data(**kwargs)
        context['title'] = self.object.vacancy.title
        context['sub_title'] = 'Предложения'
        context['success_message'] = 'Изменения сохранены'
        context['submit_title'] = 'Сохранить'
        context['form_action'] = reverse_lazy('company:vacancy_offer_update', kwargs={
            'vacancy_id': self.object.vacancy.pk,
            'pk': self.object.pk,
        })
        context['success'] = self.request.GET.get('SAVED') == 'Y'
        return context


def vacancy(request, pk):
    title = 'детали продукта'
    # links_menu = companyapp_models.Vacancy.objects.all()
    vacancy = get_object_or_404(companyapp_models.Vacancy, pk=pk)

    context = {
        'title': title,
        'vacancy': vacancy,
    }

    return render(request, 'mainapp/vacancy.html', context=context)


def company(request, pk):
    title = 'Компания'
    # links_menu = companyapp_models.Vacancy.objects.all()
    company = get_object_or_404(CompanyProfile, pk=pk)

    context = {
        'title': title,
        'company': company,
    }

    return render(request, 'mainapp/company.html', context=context)


def apply_to_vacancy(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    user_id = request.user.id
    if request.method == 'POST':
        form = ApplyForm(user_id=user_id, data=request.POST)
        if form.is_valid():
            resume_id = form.cleaned_data['resume'].id
            Response.objects.create(resume=Resume.objects.get(pk=resume_id),
                                    status=Status.objects.get(title='ожидание ответа'),
                                    vacancy=Vacancy.objects.get(pk=pk),
                                    cover_letter=request.POST['cover_letter'], date=datetime.now())
            return render(request, 'mainapp/apply_vacancy_success.html', {'vacancy': vacancy})
    else:
        form = ApplyForm(user_id=user_id)
    return render(request, 'mainapp/apply_to_vacancy.html', {'form': form, 'vacancy': vacancy})


# Контроллер для списка резюме
class ResumeListView(ListView):
    template_name = 'mainapp/resume_list.html'
    model = Resume
    paginate_by = 10
    ordering = ['id']

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ResumeListView, self).get_context_data(**kwargs)
        context['title'] = 'Мои резюме'

        return context


# Контроллер добавления резюме*
class ResumeCreateView(CreateView):
    template_name = 'mainapp/resume_form.html'
    model = Resume
    form_class = ResumeForm

    # def get_form(self):
    #     return self.form_class(initial={'visible': True})

    def get_success_url(self):
        return reverse_lazy('jobfinder:resume_add') + '?ADDED=Y'

    def form_valid(self, form):

        form.instance.user = self.request.user
        if form.is_valid():
            res = form.save(commit=True)

        exp_form = ExperienceFormSet(self.request.POST, instance=res)
        exp_form.instance.resume = res

        if exp_form.is_valid():
            exp_form.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ResumeCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Добавление резюме'
        context['success_message'] = 'Резюме добавлено'
        context['submit_title'] = 'Добавить'
        context['form_action'] = reverse_lazy('jobfinder:resume_add')
        context['success'] = self.request.GET.get('ADDED') == 'Y'
        context['experience_form'] = ExperienceFormSetCreate()
        return context


# Контроллер редактирования резюме*
class ResumeUpdateView(UpdateView):
    template_name = 'mainapp/resume_form.html'
    model = Resume
    form_class = ResumeForm

    def form_valid(self, form, **kwargs):
        exp_form = ExperienceFormSet(
            form.data, instance=self.get_object())

        if exp_form.is_valid():
            exp_form.save()

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

        # context['experience_form'] = [ExperienceForm(instance=exp) for exp in Experience.objects.filter(
        # resume_id=self.object.pk)]
        context['experience_form'] = ExperienceFormSet(instance=self.get_form().instance)

        return context


# Контроллер удаления резюме
def delete_resume(request, pk):
    resume_obj = Resume.objects.filter(id=pk).first()
    resume_obj.delete()

    return HttpResponseRedirect(reverse_lazy('jobfinder:my-resumes'))


# Контроллер отображения всех видимых резюме

class ResumesAllListView(ListView):
    template_name = 'mainapp/all_resumes_list.html'
    model = Resume
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(visible=True)

    def get_context_data(self, **kwargs):
        context = super(ResumesAllListView, self).get_context_data(**kwargs)
        context['title'] = 'Кандидаты'

        return context


class ResumeDetailView(DetailView):
    template_name = 'mainapp/resume_detail.html'
    model = Resume

    def get_context_data(self, **kwargs):
        context = super(ResumeDetailView, self).get_context_data(**kwargs)
        context['title'] = "Просмотр резюме"
        context['first_name'] = JobFinderProfile.objects.filter(user=self.object.user.id).first().first_name
        context['last_name'] = JobFinderProfile.objects.filter(user=self.object.user.id).first().last_name
        context['age'] = JobFinderProfile.objects.filter(user=self.object.user.id).first().age
        context['phone'] = JobFinderProfile.objects.filter(user=self.object.user.id).first().phone
        context['country'] = JobFinderProfile.objects.filter(user=self.object.user.id).first().country
        context['city'] = JobFinderProfile.objects.filter(user=self.object.user.id).first().city
        context['experience'] = Experience.objects.filter(resume=self.object.pk)
        # print(context)
        return context


# Контроллер для спика откликов
class ResponseListView(ListView):
    template_name = 'mainapp/response_list.html'
    model = Response
    paginate_by = 10
    ordering = ['id']

    def get_queryset(self):
        return super().get_queryset().filter(resume__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ResponseListView, self).get_context_data(**kwargs)
        context['title'] = 'Мои отклики'

        return context


# Контроллер для списка предложений
class OfferListView(ListView):
    template_name = 'mainapp/offer_list.html'
    model = Offer
    paginate_by = 10
    ordering = ['id']

    def get_queryset(self):
        return super().get_queryset().filter(resume__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(OfferListView, self).get_context_data(**kwargs)
        context['title'] = 'Мои предложения'
        context['status_form'] = OfferApplyForm
        context['success_message'] = 'Изменения сохранены'
        context['submit_title'] = 'Сохранить'
        return context


# Изменение статуса предложения
class OfferApplyView(UpdateView):
    template_name = 'mainapp/offer_response_form.html'
    model = Offer
    form_class = OfferForm

    def get_success_url(self):
        return reverse_lazy('jobfinder:offer-edit', kwargs={
            'pk': self.object.pk,
        }) + '?SAVED=Y'

    def get_context_data(self, **kwargs):
        context = super(OfferApplyView, self).get_context_data(**kwargs)
        context['title'] = self.object.vacancy.title
        context['sub_title'] = 'Предложения'
        context['success_message'] = 'Изменения сохранены'
        context['submit_title'] = 'Сохранить'
        context['form_action'] = reverse_lazy('jobfinder:offer-edit', kwargs={
            'pk': self.object.pk,
        })
        context['success'] = self.request.GET.get('SAVED') == 'Y'
        return context


def apply_to_resume(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    company_id = request.user.id
    if request.method == 'POST':
        form = AddPostForm(company_id=company_id, data=request.POST)
        if form.is_valid():
            vacancy_id = form.cleaned_data['vacancy'].id
            Offer.objects.create(vacancy=Vacancy.objects.get(pk=vacancy_id),
                                 status=Status.objects.get(title='ожидание ответа'),
                                 resume=Resume.objects.get(pk=pk),
                                 cover_letter=request.POST['cover_letter'], date=datetime.now())
            return render(request, 'mainapp/addpage_success.html', {'resume': resume})
    else:
        form = AddPostForm(company_id=company_id)
    return render(request, 'mainapp/addpage.html', {'form': form, 'resume': resume})


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'mainapp/addpage.html'
    success_url = reverse_lazy('mainapp/addpage_success.html')
