from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    email = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s Profile"
