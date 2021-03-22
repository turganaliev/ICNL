from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

ADMIN = 1
CLIENT = 2

user_types = (
    (ADMIN, 'ADMIN'),
    (CLIENT, 'CLIENT'),
)


class User(AbstractUser):
    phone = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    role = models.IntegerField(choices=user_types, default=ADMIN)


class Code(models.Model):
    conf_code = models.CharField(max_length=6)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    valid_until = models.DateTimeField(blank=True)
