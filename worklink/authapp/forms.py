import hashlib
import random

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, \
    UserChangeForm
from django import forms
from django.contrib.auth.models import User

from authapp.models import User, UserProfile


# форма для регистрации нового пользователя
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        # экранная форма на основе модели User с полями
        fields = ('username', 'password1', 'password2', 'email',)

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
        model = User
        fields = ('username', 'first_name', 'email', 'age', 'avatar',
                  'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")
        return data


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
        model = UserProfile
        fields = (
            'phone', 'gender', 'birthday', 'country', 'city', 'is_employer')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
