import datetime
from django.conf import settings
from django.utils import timezone

expire_date = settings.JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': user.username,
        'expire_date': timezone.now() + expire_date -datetime.timedelta(seconds=200)
    }