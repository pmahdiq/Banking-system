from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=20, unique=True)
    age = models.CharField(max_length=3)
    number = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    hashed_password = models.CharField()

    def __str__(self):
        return f"{self.name} ({self.username})"

