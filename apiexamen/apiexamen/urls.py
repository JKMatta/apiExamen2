from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

from apiexm.views import UsuarioViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'Usuarios', UsuarioViewSet)

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]