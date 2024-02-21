from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneNumberField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

