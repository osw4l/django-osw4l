from django.urls import path, include
from .views import HomeTemplateView, log_out, ProjectListView, ProjectDetailView
app_name = 'niza'

urlpatterns = [
    path('home/', HomeTemplateView.as_view(), name='home'),
    path('log_out/', log_out, name='log_out'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project')

]
