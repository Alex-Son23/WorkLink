# Форма для новой вакансии
from django import forms

from companyapp.models import VacancyListModel


class VacancyForm(forms.ModelForm):
    class Meta:
        model = VacancyListModel
        fields = ('title', 'celery', 'body',)

    def __init__(self, *args, **kwargs):
        super(VacancyForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
