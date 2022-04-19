from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


def send_email_for_verify(request, user, use_https=False):
    current_site = get_current_site(request)
    context = {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token_generator.make_token(user),
        'protocol': 'https' if use_https else 'http',
    }

    message = render_to_string(
        'personal/verify_email.html',
        context=context
    )
    email = EmailMessage(
        'Verify email',
        message,
        to=[user.email],
    )
    email.send()
