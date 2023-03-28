# Форма для новой вакансии
from django import forms
from companyapp.models import Vacancy


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = '__all__'
        exclude = ('is_closed', 'created_at', 'updated_at', 'company_id', )

    def __init__(self, *args, **kwargs):
        super(VacancyForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.input_type == 'checkbox':
                field.widget.attrs['class'] = 'custom-control-input'
                field.label_suffix = ''
            else:
                field.widget.attrs['class'] = 'form-control'
