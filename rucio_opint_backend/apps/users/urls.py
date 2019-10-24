from django.urls import path, include

from rucio_opint_backend.apps.users.views import CERNLogin

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth-registration/', include('rest_auth.registration.urls')),
    path('rest-auth/cern/', CERNLogin.as_view(), name='cern_login')
]
