from django.db import transaction
from django.contrib import auth
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import UserRegisterForm, UserEditForm, UserLoginForm, \
    UserProfileForm, CompanyProfileForm

from authapp.models import CompanyProfile, JobFinderProfile

from worklink import settings
'''
Функция ниже понадобится в будущем, функция отправки сообщения
'''


def send_verify_mail(user):
    # verify_link = reverse('auth:verify', args=[user.email, user.activation_key])

    title = f'Регистрация в WorkLink'

    message = f'Вы успешно зарегестрированы {user.username}!' \
              f'Наш сервис поможет вам найти работу!'

    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


# Аутентификация пользователя
def login(request):
    title = 'Вход'
    login_form = UserLoginForm(data=request.POST or None)
    # предварительная аутентификации для перехода к страницам
    next = request.GET['next'] if 'next' in request.GET.keys() else ''

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        # процедура аутентификации
        user = auth.authenticate(username=username, password=password)

        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('index'))

    content = {
        'title': title,
        'login_form': login_form,
        'next': next,
    }
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


# Регистрация пользователя
def register(request):
    title = 'Регистрация'

    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            user = register_form.save()
            # перенаправление на страницу аутентификации
            # return HttpResponseRedirect(reverse('auth:login'))

            # '''
            # Функция ниже понадобится в будущем, функция отправки сообщения
            # '''
            if send_verify_mail(user):
                print('сообщение подтверждения отрпавлено')
                return HttpResponseRedirect(reverse('auth:login'))
            else:
                print('ошибка отправки сообщения')
                return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = UserRegisterForm()

    content = {
        'title': title,
        'register_form': register_form
    }
    return render(request, 'authapp/register.html', content)


@transaction.atomic()
def edit(request):
    title = 'редактирование'

    if request.method == 'POST':
        edit_form = UserEditForm(request.POST, request.FILES,
                                 instance=request.user)

        if request.user.status == 'соискатель':
            profile = JobFinderProfile.objects.filter(user=request.user)[0]
            profile_form = UserProfileForm(
                request.POST,
                instance=profile)
        elif request.user.status == 'компания':
            company = CompanyProfile.objects.filter(user=request.user)[0]
            profile_form = CompanyProfileForm(
                request.POST,
                instance=company)

        # profile_form = UserProfileForm(request.POST,
        #                                instance=request.user.userprofile)
        if edit_form.is_valid() and profile_form.is_valid():
            print('HUI')
            edit_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = UserEditForm(instance=request.user)
        if request.user.status == 'соискатель':
            profile = JobFinderProfile.objects.filter(user=request.user)[0]
            end_form = UserProfileForm(
                instance=profile)
        elif request.user.status == 'компания':
            company = CompanyProfile.objects.filter(user=request.user)[0]
            end_form = CompanyProfileForm(
                instance=company
            )

    content = {
        'title': title,
        'edit_form': edit_form,
        'profile_form': end_form,
    }

    return render(request, 'authapp/edit.html', content)

#
# '''
# Функция ниже понадобится в будущем, функция верификации пользователя
# '''
# def verify(request, email, activation_key):
#     try:
#         user = ShopUser.objects.get(email=email)
#         if user.activation_key == activation_key and not user.is_activation_key_expired():
#             user.is_active = True
#             user.save()
#             auth.login(request, user)
#             return render(request, 'authapp/verification.html')
#         else:
#             print(f'error activation user: {user}')
#             return render(request, 'authapp/verification.html')
#     except Exception as e:
#         print(f'error activation user: {e.args}')
#         return HttpResponseRedirect(reverse('index'))
