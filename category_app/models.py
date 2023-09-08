from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    description = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.description