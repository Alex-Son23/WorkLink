
# Форма для новой вакансии
from django import forms
from jobfinderapp.models import Resume, Experience



class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = '__all__'
        exclude = ('is_closed', 'created_at', 'updated_at', 'user_id')

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

