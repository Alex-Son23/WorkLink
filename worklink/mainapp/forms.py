# Форма для новой вакансии
from django import forms
from mainapp.models import Resume, Experience, Vacancy, Response, Offer


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        exclude = ('is_closed', 'created_at', 'updated_at', 'user')

    def is_valid(self) -> bool:
        return super().is_valid()

    def __init__(self, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            try:
                if field.widget.input_type == 'checkbox':
                    field.widget.attrs['class'] = 'custom-control-input'
                    field.label_suffix = ''
                else:
                    field.widget.attrs['class'] = 'form-control'
            except AttributeError:
                pass


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
        exclude = ('resume',)

    def __init__(self, *args, **kwargs):
        super(ExperienceForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            try:
                if field.widget.input_type == 'checkbox':
                    field.widget.attrs['class'] = 'custom-control-input'
                    field.label_suffix = ''
                else:
                    field.widget.attrs['class'] = 'form-control'
            except AttributeError:
                pass


ExperienceFormSet = forms.inlineformset_factory(
    Resume,
    Experience,
    ExperienceForm,
    fields='__all__',
    # max_num=2,
    extra=1,
    can_delete=True,
)

ExperienceFormSetCreate = forms.inlineformset_factory(
    Resume,
    Experience,
    ExperienceForm,
    fields='__all__',
    # max_num=2,
    extra=1,
    can_delete=False,
)


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = '__all__'
        exclude = ('is_closed', 'created_at', 'updated_at', 'company',)

    def __init__(self, *args, **kwargs):
        super(VacancyForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.input_type == 'checkbox':
                field.widget.attrs['class'] = 'custom-control-input'
                field.label_suffix = ''
            else:
                field.widget.attrs['class'] = 'form-control'


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ('status', )

    def __init__(self, *args, **kwargs):
        super(ResponseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class OfferForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ('status', )

    def __init__(self, *args, **kwargs):
        super(OfferForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ApplyForm(forms.ModelForm):
    resume = forms.ModelChoiceField(
        queryset=None,  
        label='Резюме',
        empty_label='Выберите резюме')
    cover_letter = forms.CharField(label='Сопроводительное письмо')
    cover_letter.widget = forms.Textarea(attrs={'class': "container mt-2 mb-3", 'rows':10, 'cols':12})

    class Meta:
        model = Response
        fields = ('cover_letter',)

    def __init__(self, user_id=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['resume'].queryset = Resume.objects.filter(user_id=user_id)


class OfferApplyForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('status', )

    def __init__(self, *args, **kwargs):
        super(OfferApplyForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class AddPostForm(forms.ModelForm):
    vacancy = forms.ModelChoiceField(
        queryset=None,
        label='Вакансия',
        empty_label='Выберите вакансию')
    cover_letter = forms.CharField(label='Сопроводительное письмо')
    cover_letter.widget = forms.Textarea(attrs={'class': "container mt-2 mb-3", 'rows': 10, 'cols': 12})

    class Meta:
        model = Offer
        fields = ('cover_letter',)

    def __init__(self, company_id=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vacancy'].queryset = Vacancy.objects.filter(company_id=company_id)
        print(self.fields['vacancy'].queryset)
