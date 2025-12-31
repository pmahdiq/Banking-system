from django.db import models
from models.Account import Account

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    amount = models.FloatField()
    type = models.CharField(
        max_length=10,
        choices=[('deposit', 'Deposit'), ('withdraw', 'Withdraw')]
    )
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} of {self.amount} in {self.account.account_number} at {self.time}"