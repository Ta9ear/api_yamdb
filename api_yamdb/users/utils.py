from django.core.mail import send_mail

from .tokens import account_activation_token


def create_user(serializer):
    """Функция создает пользователя и отправляет ему письмо."""
    email = serializer.validated_data['email']
    user = serializer.save(is_active=False, role='user')
    mail_subject = 'Your activation code'
    token = account_activation_token.make_token(user)
    message = f'Hi! Here is your confirmation code: {token}'
    return send_mail(mail_subject, message, 'from@example.com', [email, ])
