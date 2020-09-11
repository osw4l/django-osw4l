from django.utils.translation import ugettext as _
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render, redirect
from .models import Project, CustomerReview
from .serializers import CustomerReviewSerializer

def log_in(request):
    context = {'error': False}
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                if user.is_superuser:
                    return redirect('admin:index')
                elif user.customer:
                    return redirect('niza:home')
            else:
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


class RateTemplateView(LoginRequiredMixin,
                       TemplateView):
    template_name = 'rate.html'


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class SendRate(GenericViewSet,
               CreateModelMixin):
    serializer_class = CustomerReviewSerializer
    queryset = CustomerReview.objects.all()
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.customer)


