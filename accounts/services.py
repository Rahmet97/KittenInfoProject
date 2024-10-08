from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_str

from .serializers import UserRegisterSerializer
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator


def register_service(request_data):
    password1 = request_data.get('password1')
    password2 = request_data.get('password2')
    email = request_data.get('email')
    username = request_data.get('username')
    if password1 == password2:
        if User.objects.filter(username=username).exists():
            return {'success': False, 'error': 'This username already exists!'}
        if User.objects.filter(email=email).exists():
            return {'success': False, 'error': 'This email already exists!'}
        serializer = UserRegisterSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return {'success': True, 'error': '', 'data': serializer.data}
    else:
        return {'success': False, 'error': 'Passwords are not same!'}


def reset_password_service(request):
    try:
        email = request.data.get('email')
        user = User.objects.get(email=email)

        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(User.pk))

        current_site = get_current_site(request)
        subject = 'Reset Password'
        msg = f'''
            User: {email}
            url: {current_site.domain}/{token}/{uid}
        '''
        send_mail(subject, msg, 'no-reply@gmail.com', [email])
    except Exception as e:
        return {'success': False, 'error': f'{e}'}
    return {'success': True, 'error': ''}


def reset_password_confirm_service(request, token, uid):
    id_ = force_str(urlsafe_base64_decode(uid))
    user = User.objects.get(pk=id_)

    if not default_token_generator.check_token(user, token):
        return {'success': False, 'error': 'Invalid token!'}
    user.set_password(request.data.get('password1'))
    user.save()
    return {'success': True, 'error': ''}
