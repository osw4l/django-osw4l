from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HomeTemplateView, log_out, ProjectListView, ProjectDetailView, RateTemplateView
from .views import SendRate
app_name = 'niza'


router = DefaultRouter()
router.register(r'rating', SendRate)


urlpatterns = [
    path('', include(router.urls)),
    path('home/', HomeTemplateView.as_view(), name='home'),
    path('rate/', RateTemplateView.as_view(), name='rate'),
    path('log_out/', log_out, name='log_out'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project')

]
