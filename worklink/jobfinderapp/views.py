from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from jobfinderapp.forms import ResumeForm, ExperienceFormSet
from jobfinderapp.models import Experience, Resume
from companyapp.models import CompanyProfile
from django.forms.models import inlineformset_factory
from django.forms import ValidationError



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

    def get_form(self):
        return self.form_class(initial={'visible': True})

    def get_success_url(self):
        return reverse_lazy('jobfinder:resume_add') + '?ADDED=Y'

    def form_valid(self, form):
        exp_form = ExperienceFormSet(form.data)
        form.instance.user_id = self.request.user

        if form.is_valid():
            res = form.save(commit=False)
        else:
            raise ValidationError(message=f'Ошибка при сохранении резюме: {form.non_form_errors()} {form.errors}')

        exp_form.instance.resume_id = res

        if exp_form.is_valid():
            exp_form.save(commit=False)
        else:
            raise ValidationError(message=f'Ошибка при сохранении опыта работы: {exp_form.non_form_errors()} {exp_form.errors}')
        
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ResumeCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Добавление резюме'
        context['success_message'] = 'Резюме добавлено'
        context['submit_title'] = 'Добавить'
        context['form_action'] = reverse_lazy('jobfinder:resume_add')
        context['success'] = self.request.GET.get('ADDED') == 'Y'
        context['experience_form'] = ExperienceFormSet()
        return context


class ResumeUpdateView(UpdateView):
    template_name = 'jobfinderapp/resume_form.html'
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
        
        # context['experience_form'] = [ExperienceForm(instance=exp) for exp in Experience.objects.filter(resume_id=self.object.pk)]
        context['experience_form'] = ExperienceFormSet(instance=self.get_form().instance)

        return context
    

class ResumeDeleteView(DeleteView):
    model = Resume
    

    def post(self, request, *args, **kwargs):
        self.model.objects.get(id=self.get_context_data().get('pk')).delete()
        return HttpResponseRedirect(self.get_success_url)

    def get_success_url(self):
        return reverse_lazy('jobfinder:my-resumes')


def delete_resume(request, pk):
    resume_obj = Resume.objects.filter(id=pk).first()
    resume_obj.delete()

    return HttpResponseRedirect(reverse_lazy('jobfinder:my-resumes'))