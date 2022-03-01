from django.db import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import CreateUserForm
from django.contrib.auth.models import User
from accounts.models import CreateUserForm
from django import forms


class KycDetails(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Bod = models.DateField(max_length=8)
    PhNumber = models.IntegerField(max_length=10)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Marital_CHOICES = (
        ('S', 'Single'),
        ('M', 'Married'),
    )
    Marital = models.CharField(max_length=1, choices=Marital_CHOICES)
    Pan = models.CharField(max_length=10)
    AadharNumber = models.IntegerField(max_length=12)
    AadharPhoto = models.ImageField(null=True)
    PanPhoto = models.ImageField(null=True)
    UserPhoto = models.ImageField(null=True)
    Signature = models.ImageField(null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.FirstName


class Ticket(models.Model):
    name = models.CharField(max_length=100)
    shortname = models.CharField(max_length=100)
    img = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Dash(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stocks = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stocks


class Wallet(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    amount = models.FloatField(default=0)
    name = models.CharField(max_length=100, default='null')

    def __str__(self):
        return self.name


class Watchlist(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.symbol


class Images(models.Model):
    image = models.ImageField(null=True)
