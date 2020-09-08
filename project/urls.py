from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter
from apps.niza.views import log_in, HomeTemplateView

router = DefaultRouter()

schema_view = get_swagger_view(title='osw4l api 2.0')

urlpatterns = [
    path('login/', log_in, name='sign_in'),
    path('', HomeTemplateView.as_view()),
    path('admin/', admin.site.urls),
    path('niza/', include('apps.niza.urls', namespace='niza')),
    path('api/', include(router.urls)),
    path('admin/statuscheck/', include('celerybeat_status.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

