from django.contrib.auth import login, logout
from django.http import HttpRequest, Http404, HttpResponse
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.views import View
from .forms import *
from utils.utils import *


class LogInView(View):
    def get(self, request):
        form = LogInForm()
        return render(request, 'login.html', {
            'form': form
        })

    def post(self, request):
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(username=username).first()

            if user is not None:
                if user.check_password(raw_password=password):
                    user.active_code = creat_random_code(6)
                    user.token = get_random_string(100)
                    user.save()
                    login(request, user)
                    return redirect('home')

                else:
                    form = LogInForm()
                    return render(request, 'login.html', {
                        'form': form,
                        'value_error': True
                    })
            else:
                form = LogInForm()
                return render(request, 'login.html', {
                    'form': form,
                    'value_error': True
                })
        else:
            form = LogInForm()
            return render(request, 'login.html', {
                'form': form,
                'value_error': True
            })


class RegisterView(View):
    def get(self, request):
        form = UserForm
        return render(request, 'register.html', {
            'form': form
        })

    def post(self, request: HttpRequest):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.active_code = creat_random_code(6)
            user.token = get_random_string(100)
            user.save()
            request.session['user_token'] = user.token

            return redirect('activation_code')

        else:
            form = UserForm
            return render(request, 'register.html', {
                'form': form,
                'value_error': True
            })


class ActivationCode(View):
    def get(self, request: HttpRequest):
        try:
            token = request.session['user_token']

        except:
            token = None

        user = User.objects.filter(token=token).first()
        if user is not None:
            return render(request, 'activation_code.html', {

            })

        else:
            raise Http404

    def post(self, request: HttpRequest):
        try:
            token = request.session['user_token']

        except:
            token = None

        user = User.objects.get(token=token)
        if user is not None:
            num1 = request.POST['num1']
            num2 = request.POST['num2']
            num3 = request.POST['num3']
            num4 = request.POST['num4']
            num5 = request.POST['num5']
            num6 = request.POST['num6']

            if user.active_code == f'{num1}{num2}{num3}{num4}{num5}{num6}':
                user.active_code = creat_random_code(6)
                user.token = get_random_string(100)
                user.save()
                login(request, user)
                return redirect('home')

        else:
            raise Http404


class ActivationCodeForgetPass(View):
    def get(self, request: HttpRequest):
        try:
            token = request.session['user_token']

        except:
            token = None

        user = User.objects.filter(token=token).first()
        if user is not None:
            return render(request, 'activation_code.html', {

            })

        else:
            raise Http404

    def post(self, request: HttpRequest):
        try:
            token = request.session['user_token']

        except:
            token = None

        user = User.objects.get(token=token)
        if user is not None:
            num1 = request.POST['num1']
            num2 = request.POST['num2']
            num3 = request.POST['num3']
            num4 = request.POST['num4']
            num5 = request.POST['num5']
            num6 = request.POST['num6']

            if user.active_code == f'{num1}{num2}{num3}{num4}{num5}{num6}':
                user.active_code = creat_random_code(6)
                user.token = get_random_string(100)
                user.save()
                request.session['user_token'] = user.token

                return redirect('new_password')

        else:
            raise Http404


class ForgetPassView(View):
    def get(self, request):
        return render(request, 'forgetpass.html', {

        })

    def post(self, request: HttpRequest):
        phone = request.POST['phone']
        user = User.objects.filter(phone=phone).first()

        if user is not None:
            request.session['user_token'] = user.token

            return redirect('activation_code_forgetpass')


        else:
            return render(request, 'forgetpass.html', {
                'value_error': True
            })


class NewPassWordView(View):
    def get(self, request):
        try:
            token = request.session['user_token']

        except:
            token = None

        user = User.objects.get(token=token)
        if user is not None:
            form = NewPassWordForm()
            return render(request, 'new_password.html', {
                'form': form
            })

        else:
            raise Http404

    def post(self, request: HttpRequest):
        token = request.session['user_token']
        user = User.objects.get(token=token)
        form = NewPassWordForm(request.POST)
        if form.is_valid():
            pass1 = form.cleaned_data.get('password1')
            pass2 = form.cleaned_data.get('password2')
            print(pass1, pass2)

            if pass1 == pass2:
                user.set_password(pass1)
                user.save()
                login(request, user)

                return redirect('home')

            else:
                form = NewPassWordForm()
                return render(request, 'new_password.html', {
                    'form': form,
                    'value_error': True
                })

        else:
            form = NewPassWordForm()
            return render(request, 'new_password.html', {
                'form': form,
                'value_error': True
            })


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
