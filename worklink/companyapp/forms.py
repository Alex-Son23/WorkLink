from django import forms
from companyapp.models import Vacancy


# class ResponseForm(forms.ModelForm):
#     # ЗАГЛУШКА для проверки! Нужно заменить Vacancy на модель Resume, когда она появится!
#     resume = forms.Select(choices=Vacancy.objects.values())
#
#     class Meta:
#         model = Vacancy
#         fields = ('title', 'salary')
    