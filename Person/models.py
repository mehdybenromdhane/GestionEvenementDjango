from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Person(AbstractUser):
    cin = models.CharField(primary_key=True, max_length=8)
    email = models.EmailField("Email",max_length=50 ,unique=True )
    username = models.CharField(max_length=20 , unique=True)

    USERNAME_FIELD='username'


    def __str__(self):
      return  self.username


    class Meta:
        verbose_name="Person"