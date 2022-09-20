from django.db import models
from  django.contrib.auth.models import User


class mobiles(models.Model):
    phone_name=models.CharField(max_length=120)
    processor=models.CharField(max_length=100)
    ram=models.PositiveIntegerField(default=4)
    price=models.PositiveIntegerField(default=10000)
    image=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.phone_name

