from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.core.validators import RegexValidator


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    description = models.TextField()
    average_score = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_description = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.price}"

phone_number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")

class UserMy(AbstractUser):
    address = models.CharField(max_length=255, blank=True)
    user_phone_number = models.CharField(
        validators=[phone_number_regex], max_length=12, unique=True,
    )
    groups = models.ManyToManyField(Group, related_name='user_my_groups')
    user_permissions = models.ManyToManyField(
        Permission, related_name='user_my_user_permissions'
    )






