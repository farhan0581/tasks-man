from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from task_app.models import CustomTokenModel
from django.utils.translation import ugettext_lazy as _


class CustomAuthentication(BaseAuthentication):
    """
    Custom authentication class which is inherited
    from drf's base class
    """

    def authenticate(self, request):
        auth_key = request.META.get('HTTP_XAUTHORIZATION')
        if not auth_key or len(auth_key) ==0:
            return None
        else:
            return self.authenticate_credentials(auth_key)

    
    def authenticate_credentials(self, key):
        model = CustomTokenModel
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        if token.is_active == 0:
            raise exceptions.AuthenticationFailed(_('Token expired'))            

        return (token.user, token)