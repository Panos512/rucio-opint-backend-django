from allauth.socialaccount.providers.cern.views import CernOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

class CERNLogin(SocialLoginView):
    adapter_class = CernOAuth2Adapter
