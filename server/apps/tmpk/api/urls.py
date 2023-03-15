from django.urls import include, path
from rest_framework import routers

from server.apps.tmpk.api.views import ContractViewSet

router = routers.DefaultRouter()
router.register(r'contracts', ContractViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
