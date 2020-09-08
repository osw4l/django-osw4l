from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render, redirect
from .models import Project


def log_in(request):
    context = {'error': False}
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print('auth ..')
        print(user)
        if user:
            if user.is_active:
                auth_login(request, user)
                if user.is_superuser:
                    print('is admin')
                    auth_login(request, user)
                    return redirect('admin:index')
                elif user.customer:
                    print('customer ..')
                    auth_login(request, user)
                    return redirect('niza:home')
            else:
                print('no one ..')
                context = {'msj': _('el usuario ha sido desactivado'), 'error': True}
        else:
            context = {'msj': _('Usuario o contraseña incorrectos'), 'error': True}
    return render(request, 'login.html', context)


@login_required
def log_out(request):
    logout(request)
    return redirect('sign_in')


class HomeTemplateView(LoginRequiredMixin,
                       TemplateView):
    template_name = 'home.html'


class ProjectListView(LoginRequiredMixin,
                      ListView):
    template_name = 'projects/list.html'
    model = Project

    def get_queryset(self):
        return self.model.objects.filter(customer=self.request.user.customer)


class ProjectDetailView(LoginRequiredMixin,
                        DetailView):
    template_name = 'projects/detail.html'
    model = Project



