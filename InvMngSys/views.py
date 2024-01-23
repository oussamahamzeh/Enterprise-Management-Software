from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.utils.http import base36_to_int
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.utils.http import int_to_base36
import logging

logger = logging.getLogger(__name__)


@login_required
def homepage(request):
    return render(request, 'homepage.html')


def invalid_link(request):
    return render(request, 'invalid_link.html')


def password_reset_confirm_custom(request, uidb64, token):
    try:
        uid = base36_to_int(uidb64)
        logger.warning(f"Decoded uidb64: {uidb64}, Decoded uid: {uid}")
        user = User.objects.get(pk=uid)

    except (ValueError, OverflowError, User.DoesNotExist) as e:
        logger.error(f"Error in password_reset_confirm_custom: {e}")
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        # The uidb64 and token are valid, show the password reset form
        return PasswordResetConfirmView.as_view()(request, uidb64=uidb64, token=token)
    else:
        # Invalid uidb64 or token, redirect to an error page or handle as needed
        ouss = get_user_model().objects.get(username='Oussama')
        logger.warning(f"Invalid uidb64 or token - uid: {uid}, token: {token},  user: {user}, Ouss: {ouss.id}")
        return HttpResponseRedirect('/invalid-link/')  # You can customize the redirect URL

