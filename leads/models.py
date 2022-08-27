from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model 

#User = get_user_model()

class User(AbstractUser):

    pass 

class Leads(models.Model):

    first_name = models.CharField(
        'Имя',
        max_length=20,
    )
    last_name  = models.CharField(
        'Фамилия',
        max_length=20
    )
    age = models.IntegerField(
        default=0
    )
    agent = models.ForeignKey(
        "Agent",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Agent(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.user.email}'


