import random
from django.core.mail import EmailMessage
from django.conf import settings
from .models import User
from . models import CustomerNumber

def generate_orderNo():
    order_no=""
    for i in range(10):
        order_no  += str(random.randint(0,9))
    return order_no

def send_orderNo(email):
    Subject = "Order Number"
    accno = generate_orderNo()
    print(accno)
    user = User.objects.get(email=email)
    body = f'Hello {user.username} thank you for choosing VickeeyMeals \n Your private number is {accno}'
    from_email = settings.DEFAULT_FROM_EMAIL

    CustomerNumber.objects.create(user=user,accno=accno)

    send_email= EmailMessage(subject=Subject, body=body, from_email=from_email, to=[email])
    send_email.send(fail_silently=True)
