from django.core.mail import send_mail

from .tokens import account_activation_token


def create_user(serializer):
    email = serializer.data['email']
    user = serializer.save(commit=False)
    user.is_active = False
    user.role = 'user'
    user.save()
    mail_subject = 'Your activation code'
    token = account_activation_token.make_token(user)
    message = f'Hi! Here is your confirmation code: {token}'
    return send_mail(mail_subject, message, 'from@example.com', [email, ])
