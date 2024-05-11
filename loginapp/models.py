from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomerNumber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    accno = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.user.username}-Private Number"
