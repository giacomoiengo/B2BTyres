from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)


class Supervisor(models.Model):
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True
    )


class Salesman(models.Model):
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True
    )
    supervisor = models.ForeignKey(
        Supervisor,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    city = models.CharField(max_length=25, null=False, blank=False)


class Customer(models.Model):
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True
    )
    salesman = models.ForeignKey(
        Salesman,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    markup = models.PositiveSmallIntegerField(null=False, blank=False)
    discount = models.PositiveSmallIntegerField(null=False, blank=False)



