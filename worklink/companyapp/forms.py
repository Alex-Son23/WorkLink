
# Форма для новой вакансии
from django import forms

from companyapp.models import JobList


class JobForm(forms.ModelForm):
    class Meta:
        model = JobList
        fields = ('title', 'celery', 'body',)

    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
