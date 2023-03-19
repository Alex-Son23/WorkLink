import hashlib
import random

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, \
    UserChangeForm
from django import forms
from django.contrib.auth.models import User

from authapp.models import WorkLinkUser, JobFinderProfile, CompanyProfile


# форма для регистрации нового пользователя
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = WorkLinkUser
        # экранная форма на основе модели User с полями
        fields = ('username', 'password1', 'password2', 'email', 'status',)

    # Метод для обеспечения стилизации элементов управления формы
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    # проверка допустимости возраста пользователя
    def clean_age(self):
        data = self.cleaned_data['age']

        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return data

    # def save(self):
    #     user = super(ShopUserRegisterForm, self).save()
    #
    #     user.is_active = False
    #     salt = hashlib.sha1(str(random.Random()).encode('utf8')).hexdigest()[
    #            :6]
    #     user.activation_key = hashlib.sha1(
    #         (user.email + salt).encode('utf8')).hexdigest()
    #     user.save()
    #
    #     return user


# форма для редактирования введенных пользователем регистрационных данных
class UserEditForm(UserChangeForm):
    class Meta:
        model = WorkLinkUser
        fields = ('username', 'email', 'avatar',
                  'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields['avatar'].widget, 'hui')
        for field_name, field in self.fields.items():
            if field_name == 'avatar':
                print(field_name, field.__dict__, field.validators[0].__dict__)
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()


# форма аутентификации пользователя
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


# форма для редактирования подробного профиля пользователя
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = JobFinderProfile
        fields = ('first_name', 'last_name', 'age', 'phone', 'gender', 'birthday', 'country', 'city',)

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            print(field_name, field)
            field.widget.attrs['class'] = 'form-control'

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return data


class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ('name', 'phone', 'country', 'city', 'description', 'greeting_letter', 'is_partner')

    def __init__(self, *args, **kwargs):
        super(CompanyProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            print(field_name, field)
            field.widget.attrs['class'] = 'form-control'


class DateInput(forms.DateInput):
    input_type = 'date'
