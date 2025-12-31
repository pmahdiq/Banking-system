from django.db import models
from models.User import User

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accounts")
    name = models.CharField(max_length=20)
    balance = models.FloatField(default=50) #change the default when ever you want
    account_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name} - {self.account_number} - {self.user.username}"