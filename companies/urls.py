from django.urls import path
from django.conf.urls import url, include

from rest_framework import routers
from companies.views import CompanyViewSet, CompanyDetailViewSet, OfficeUpdateView

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'companies', CompanyDetailViewSet)
router.register(r'offices', OfficeUpdateView)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]