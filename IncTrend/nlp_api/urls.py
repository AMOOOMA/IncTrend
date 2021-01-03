from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'Messages', views.MessageViewSet)
router.register(r'Company', views.CompanyViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^predictions/(?P<name>[a-zA-Z]*)$', views.handle_company_query),
]
